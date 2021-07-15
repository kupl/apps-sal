import sys

input = sys.stdin.readline
n,m = list(map(int,input().split()))
from collections import defaultdict
dic = defaultdict(list)

for _ in range(m):
    u,v = list(map(int,input().split()))
    dic[u-1].append(v-1+n)
    dic[u - 1+n].append(v - 1 + 2*n)
    dic[u - 1+2*n].append(v - 1)

G = dic
s,t = list(map(int,input().split()))

# G[v]: 頂点vに隣接する頂点list
# N: 頂点数

from collections import deque
dist = [-1]*(n*3)
que = deque([s-1])
dist[s-1] = 0
while que:
    v = que.popleft()
    d = dist[v]
    for w in G[v]:
        if dist[w] > -1:
            continue
        dist[w] = d + 1
        que.append(w)
print((dist[t-1]//3))


