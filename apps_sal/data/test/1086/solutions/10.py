(H, W) = map(int, input().split())
AB = []
max_ab = 0
for i in range(H):
    AB.append(list(map(int, input().split())))
    max_ab = max(max_ab, max(AB[-1]))
for i in range(H):
    AB[i] = [abs(AB[i][j] - int(b)) for (j, b) in enumerate(input().split())]
base = max_ab * (H + W)
dp = [[1 << base for w in range(W)] for h in range(H)]
dp[0][0] = 1 << base + AB[0][0] | 1 << base - AB[0][0]
for h in range(1, H):
    dp[h][0] = dp[h - 1][0] << AB[h][0] | dp[h - 1][0] >> AB[h][0]
for w in range(1, W):
    dp[0][w] = dp[0][w - 1] << AB[0][w] | dp[0][w - 1] >> AB[0][w]
for h in range(1, H):
    for w in range(1, W):
        dp[h][w] = dp[h - 1][w] << AB[h][w] | dp[h - 1][w] >> AB[h][w] | dp[h][w - 1] << AB[h][w] | dp[h][w - 1] >> AB[h][w]
positive = bin(dp[H - 1][W - 1] >> base)
print(positive[::-1].find('1'))
