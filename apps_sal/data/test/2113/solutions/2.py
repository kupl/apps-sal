from collections import deque

n = int(input())
g = [[] for i in range(n+1)]
for i in range(n-1):
    u, v = list(map(int, input().split()))
    g[u].append(v)
    g[v].append(u)
    
f = [0]*(n+1)
c = [1, 0]
q = deque()
q.appendleft((1, 0))
while q:
    u, p = q.pop()
    for v in g[u]:
        if v != p:
            f[v] = (f[u] + 1) % 2
            c[f[v]] += 1
            q.appendleft((v, u))

ans = 0
for u in range(1, n+1):
    n = len(g[u])
    opp = c[1-f[u]]
    ans += opp - n
    
print(ans // 2)

