(N, X, M) = map(int, input().split())
id = [-1] * M
a = list()
l = 0
total = 0
while id[X] < 0:
    id[X] = l
    a.append(X)
    total += X
    l += 1
    X = pow(X, 2, M)
c = l - id[X]
s = 0
for i in range(id[X], l, 1):
    s += a[i]
ans = 0
if N <= l:
    for i in range(N):
        ans += a[i]
else:
    ans += total
    N -= l
    ans += N // c * s
    N %= c
    for i in range(N):
        ans += a[id[X] + i]
print(ans)
