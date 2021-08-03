N = int(input())
A = list(map(int, input().split()))
INF = 10**18

dp0 = 0
dp1 = -INF
dp2 = -INF

for i, a in enumerate(A):
    if i % 2 == 0:
        dp1 = max(dp1, dp0)
        dp0 += a
        dp2 += a
    else:
        dp2 = max(dp2, dp1)
        dp1 += a

if N % 2 == 1:
    print((max(dp1, dp2)))
else:
    print((max(dp0, dp1)))
