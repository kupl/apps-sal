(n, m) = map(int, input().split())
(X, Y) = ({}, {})
for i in range(n):
    (x, u) = map(int, input().split())
    p = x * u
    if p in X:
        X[p] += 1
    else:
        X[p] = 1
for i in range(m):
    (y, v) = map(int, input().split())
    p = y * v
    if p in Y:
        Y[p] += 1
    else:
        Y[p] = 1
ans = 0
for i in X:
    if i in Y:
        ans += min(X[i], Y[i])
print(ans)
