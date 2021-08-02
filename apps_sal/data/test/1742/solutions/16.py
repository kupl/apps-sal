n, m = list(map(int, input().split()))

q = list(map(int, input().split()))

G = [set() for _ in range(n + 1)]
vn = []
for i in range(m):
    u, v = list(map(int, input().split()))
    G[u].add(v)

P = set([q[-1]])
for i in range(n - 2, -1, -1):
    p = q[i]
    if len(G[p]) < len(P) or not P.issubset(G[p]):
        P.add(p)
print(n - len(P))
