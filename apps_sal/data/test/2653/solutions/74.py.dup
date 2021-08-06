N, Q = map(int, input().split())
G = [[] for n in range(N)]
ans = N * [0]

for n in range(N - 1):
    a, b = map(int, input().split())
    G[a - 1].append(b - 1)
    G[b - 1].append(a - 1)

for q in range(Q):
    p, x = map(int, input().split())
    ans[p - 1] += x

f = N * [1]
t = [0]
while t:
    v = t.pop()
    f[v] = 0
    for k in G[v]:
        if f[k]:
            ans[k] += ans[v]
            t.append(k)

print(*ans)
