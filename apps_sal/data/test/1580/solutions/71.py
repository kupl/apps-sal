(N, M) = list(map(int, input().split()))
par = [-1] * N


def find(x):
    if par[x] < 0:
        return x
    else:
        par[x] = find(par[x])
        return par[x]


def union(x, y):
    (p, q) = (find(x), find(y))
    if p == q:
        return
    if p > q:
        (p, q) = (q, p)
    par[p] += par[q]
    par[q] = p


for _ in range(M):
    (X, Y, _) = list(map(int, input().split()))
    (X, Y) = (X - 1, Y - 1)
    union(X, Y)
ans = 0
for i in range(N):
    if par[i] < 0:
        ans += 1
print(ans)
