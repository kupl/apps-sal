(H, W) = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]
dp = [[0] * (W + 1) for _ in range(H + 1)]
F = 80 * 200 + 100
dp[0][0] = 1 << F
for h in range(H):
    for w in range(W):
        a = A[h][w]
        b = B[h][w]
        d = dp[h][w]
        dp[h + 1][w] |= d << abs(a - b) | d >> abs(a - b)
        dp[h][w + 1] |= d << abs(a - b) | d >> abs(a - b)
res = dp[H][W - 1] | dp[H - 1][W]
ans = 10 ** 18
for d in range(F * 2):
    if res & 1 << d != 0:
        ans = min(ans, abs(d - F))
print(ans)
