n, m, k = list(map(int, input().split()))
special = list(map(int, input().split()))

root = [p for p in range(n + 1)]


def par(p):
    if p != root[p]:
        root[p] = par(root[p])
    return root[p]


for i in range(m):
    u, v = list(map(par, list(map(int, input().split()))))
    root[v] = u

sz = [0 for i in range(n + 1)]

for i in range(n + 1):
    sz[par(i)] += 1

leftover = n
ans = 0
largest = 0

for x in special:
    d = par(x)
    largest = max(largest, sz[d])
    ans += sz[d] * (sz[d] - 1) // 2
    leftover -= sz[d]

ans -= largest * (largest - 1) // 2
ans += (largest + leftover) * ((largest + leftover) - 1) // 2
ans -= m
print(ans)
