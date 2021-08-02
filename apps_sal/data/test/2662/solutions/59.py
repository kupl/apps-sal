import bisect
n, *a = list(map(int, open(0).read().split()))
a = a[::-1]
INF = 1 << 30
dp = [INF] * (n + 1)

for e in a:
    dp[bisect.bisect_right(dp, e)] = e
print((bisect.bisect_left(dp, INF)))
