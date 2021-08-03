n, m = map(int, input().split())
a = [None] * m
c = [0] * m
for i in range(m):
    a[i], b = map(int, input().split())
    ls = list(map(int, input().split()))
    for j in ls:
        c[i] |= 1 << (j - 1)
n2 = 1 << n
dp = [1e9] * (n2)
dp[0] = 0
for i in range(m):
    for S in range(n2):
        if dp[S | c[i]] > dp[S] + a[i]:
            dp[S | c[i]] = dp[S] + a[i]
if dp[(n2) - 1] < 1e9:
    print(dp[(n2) - 1])
else:
    print(-1)
