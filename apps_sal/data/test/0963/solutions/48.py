N, K = map(int, input().split())
S = []
for _ in range(K):
    L, R = map(int, input().split())
    S.append([L, R])
a = [0] * (N + 1)
d = [0] * (3 * N)
d[0] = 1  # d[i] = a[i+1]-a[i]
d[1] = -1
for i in range(1, N + 1):
    a[i] = (a[i - 1] + d[i - 1]) % 998244353
    for l, r in S:
        d[i + l - 1] += a[i]
        d[i + r] -= a[i]
print(a[N])
