def get(px, py, x, y):
    ans = 10**18
    nonlocal k
    if px <= k:
        cnt = (px + x + k - 1) // k - 1
        if y == cnt:
            ans = min(ans, px + x - cnt * k)
        elif y > cnt and y <= x * k:
            ans = min(ans, 1)
    if py <= k:
        cnt = (x + k - 1) // k - 1
        if y == cnt:
            ans = min(ans, x - cnt * k)
        elif y > cnt and y <= (x - 1) * k + (k - py):
            ans = min(ans, 1)
    return ans


n, k = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
dp = [[10**18] * (n + 1), [10**18] * (n + 1)]
dp[0][0], dp[1][0] = 0, 0
for i in range(n):
    dp[0][i + 1] = get(dp[0][i], dp[1][i], x[i], y[i])
    dp[1][i + 1] = get(dp[1][i], dp[0][i], y[i], x[i])
print('YES' if min(dp[0][-1], dp[1][-1]) <= k else 'NO')
