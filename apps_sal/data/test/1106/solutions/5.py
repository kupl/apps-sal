n = int(input())
a = list(map(int, input().split()))
dp = [0] * (2 ** (n + 1) - 1)
for i in range(2, 2 ** (n + 1)):
    dp[i - 1] = dp[i // 2 - 1] + a[i - 2]
mx = 0
sm = 0
# print(dp)
x = [0] * (2 ** (n + 1) - 1)
for i in range(2 ** n):
    mx = max(mx, dp[-i - 1])
    sm += dp[-i - 1]
for i in range(2 ** n):
    x[-i - 1] = mx - dp[-i - 1]
# print(x)
i = len(x) - 1
while i >= 0:
    mn = min(x[i], x[i - 1])
    x[i] -= mn
    x[i - 1] -= mn
    x[(i + 1) // 2 - 1] += mn
    i -= 2
print(sum(x))
