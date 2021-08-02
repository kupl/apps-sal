tdlist = lambda i, j, value=0: [[value] * j for _ in range(i)]

h, w = list(map(int, input().split()))
D = 160 * 80
D2 = D * 2 + 1

diff = [list(map(int, input().split())) for _ in range(h)]
for i in range(h):
    for j, b in enumerate(list(map(int, input().split()))):
        diff[i][j] = abs(diff[i][j] - b)

dp = tdlist(h, w)
dp[0][0] |= 1 << D + diff[0][0]
dp[0][0] |= 1 << D - diff[0][0]

for i in range(h):
    for j in range(w):
        if j:
            dp[i][j] |= dp[i][j - 1] << diff[i][j]
            dp[i][j] |= dp[i][j - 1] >> diff[i][j]
        if i:
            dp[i][j] |= dp[i - 1][j] << diff[i][j]
            dp[i][j] |= dp[i - 1][j] >> diff[i][j]

ans = float("inf")
for i in range(D2):
    if dp[h - 1][w - 1] >> i & 1:
        ans = min(ans, abs(i - D))
print(ans)
