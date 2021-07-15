import sys
n, m = map(int, input().split())
 
g = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    g[u-1].append(v-1)
    g[v-1].append(u-1)

N = n-1
for i in g[0]:
    if N in g[i]:
        print('POSSIBLE')
        return

print('IMPOSSIBLE')
