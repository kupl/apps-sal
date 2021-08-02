N, X, M = map(int, input().split())
id = [-1] * M
l = 0
total = 0
a = list()
while(id[X] == -1):
    a.append(X)
    id[X] = l
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
    ans += s * (N // c)
    N %= c
    for i in range(N):
        ans += a[id[X] + i]
print(ans)
