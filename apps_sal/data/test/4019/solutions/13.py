import sys
from collections import deque
sys.setrecursionlimit(20000000)
input = sys.stdin.readline
n,m,d = map(int,input().split())
g = [[] for i in range(n)]
for i in range(m):
        a,b = map(int,input().split())
        a-=1;b-=1
        g[a].append(b)
        g[b].append(a)

ne = 0


ans = []
mita = [0]*n
mita[ne] = -1
def dfs(x,y):
        for i in g[x]:
                if mita[i] == 0:
                        ans.append([x+1,i+1])
                        mita[i] = y
                        que.append([i,y])
for i in g[ne]:
        if mita[i] != 0:
                continue
        mita[i] = i
        que = deque()
        que.append([i,i])
        while que:
                x,y = que.popleft()
                dfs(x,y)
syo = len(set(mita))-1
if syo > d or len(g[ne]) < d:
        print("NO")
        return
print("YES")
use = set()
ki  = set()
for i in g[ne]:
        if mita[i] in ki:
                continue
        else:
                ki.add(mita[i])
                use.add(i)
for i in g[ne]:
        if len(use) == d:
                break
        if i not in use:
                use.add(i)

g[ne] = list(use)
ans = []
mita = [0]*n
mita[ne] = 1
def dfs(x):
        for i in g[x]:
                if mita[i] == 0:
                        ans.append([x+1,i+1])
                        mita[i] = 1
                        que.append(i)
que = deque()
que.append(ne)
while que:
        dfs(que.popleft())
for i,j in ans:
        print(i,j)
