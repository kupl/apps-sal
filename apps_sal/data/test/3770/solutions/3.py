
"""

https://atcoder.jp/contests/arc107/tasks/arc107_f

絶対値なので、頂点を正側・府側に割り当てて、その間に辺があってはいけない
とする
頂点が消える場合もある…

全部正の寄与として答えにあらかじめ足しておく
元が+の場合、 -側にあると -2A の被害・消されると-Aの被害
元が-の場合、 +側にあると -2A の被害・消されると-Aの被害

基本的に別側にあると被害のみ記述できる
頂点を2倍する…しか考えられない

(+基準点)
||
aA
と2つ繋げると、両方反対側で-2A・片方だけ反対で-A・両方基準点側で-0を表現できる

bB
||
(-基準点)

start 
|| ||  ←+側
------
|| ||
aA bB  ←-側
|| ||
|| ||
 GOAL


aA/
a/A
/aA
の3通りに絞る
Aが+側になる & bが負側はまずい
→inf

"""

import sys
from sys import stdin

from collections import defaultdict
from collections import deque
import sys
sys.setrecursionlimit(200000)

def Dinic_DFS(v,g,maxflow,lines,cost,level):
    if v == g:
        return maxflow

    realflow = 0
    tmp = [i for i in lines[v]]
    for nex in tmp:
        if level[nex] > level[v]:
            
            plusflow = Dinic_DFS(nex,g,min(maxflow , cost[v][nex]),lines,cost,level)
            cost[v][nex] -= plusflow
            if cost[v][nex] == 0:
                lines[v].remove(nex)
            if cost[nex][v] == 0:
                lines[nex].add(v)
            cost[nex][v] += plusflow
            
            realflow += plusflow
            maxflow -= plusflow

            if maxflow <= 0:
                return realflow

    return realflow

def Dinic(s,g,lines,cost):

    N = len(cost)
    ans = 0

    while True:

        #bfs
        q = deque([s])
        level = [float("inf")] * N
        level[s] = 0
        while q:
            now = q.popleft()
            for nex in lines[now]:

                if level[nex] > level[now] + 1:
                    level[nex] = level[now] + 1
                    q.append(nex)

        if level[g] == float("inf"):
            return ans

        #dfs
        delta_flow = Dinic_DFS(s,g,float("inf"),lines,cost,level)
        while delta_flow > 0:
            ans += delta_flow
            delta_flow = Dinic_DFS(s,g,float("inf"),lines,cost,level)

inf = 10**18
N,M = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))

s  = 2*N
g  = 2*N+1

ans = 0
for i in range(N):
    ans += abs(B[i])

lines = defaultdict(set)
cost = [ [0] * (2*N+2) for i in range(2*N+2) ]

for i in range(N):

    lines[i+N].add(i)
    cost[i+N][i] += inf

    if B[i] >= 0:
        
        lines[s].add(i)
        cost[s][i] += 2*B[i]

        lines[i].add(N+i)
        cost[i][N+i] += A[i]+B[i]
    
    elif B[i] < 0:

        lines[i].add(N+i)
        cost[i][N+i] += A[i]+abs(B[i])

        lines[i+N].add(g)
        cost[i+N][g] += 2*abs(B[i])

for i in range(M):
    u,v = map(int,stdin.readline().split())
    u -= 1
    v -= 1

    lines[u+N].add(v)
    cost[u+N][v] += inf

    lines[v+N].add(u)
    cost[v+N][u] += inf

print (ans - Dinic(s,g,lines,cost))
