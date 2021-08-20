def cmp(a, b, c):
    if b == -1:
        return a
    if a == -1 or b + c < a:
        return b + c
    return a


n = int(input())
cs = list(map(int, input().split()))
dp = [[-1, -1] for i in range(n)]
dp[0][0] = 0
dp[0][1] = cs[0]
last = input()
for i in range(1, n):
    s = input()
    rlast = last[::-1]
    rs = s[::-1]
    if s >= last:
        dp[i][0] = cmp(dp[i][0], dp[i - 1][0], 0)
    if s >= rlast:
        dp[i][0] = cmp(dp[i][0], dp[i - 1][1], 0)
    if rs >= last:
        dp[i][1] = cmp(dp[i][1], dp[i - 1][0], cs[i])
    if rs >= rlast:
        dp[i][1] = cmp(dp[i][1], dp[i - 1][1], cs[i])
    last = s
if dp[n - 1][0] == -1:
    print(dp[n - 1][1])
elif dp[n - 1][1] == -1:
    print(dp[n - 1][0])
else:
    print(min(dp[n - 1][0], dp[n - 1][1]))
