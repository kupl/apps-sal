
import numpy
n, t = map(int, input().split())
time = []
for i in range(n):
    x, y = map(int, input().split())
    time.append((x, y))


dp = numpy.zeros(t, dtype=int)
time.sort()
ans = 0
for a, b in time:
    ans = max(ans, dp[-1] + b)
    dp[a:] = numpy.maximum(dp[a:], dp[:-a] + b)

print(ans)
