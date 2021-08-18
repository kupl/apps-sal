

H, W = list(map(int, input().split()))

amap = [list(map(int, input().split())) for i in range(H)]
bmap = [list(map(int, input().split())) for i in range(H)]
dist_map = [[amap[y][x] - bmap[y][x] for x in range(W)] for y in range(H)]

mid = 80 * 80 * 5 // 2
# mid = 20
dp = [[1 << mid] * W for y in range(H)]

dp[0][0] = ((1 << (dist_map[0][0] + mid)) | (1 << (mid - dist_map[0][0])))


for x in range(1, W):
    y = 0
    d = abs(dist_map[y][x])
    dp[y][x] = (dp[y][x - 1] << d) | (dp[y][x - 1] >> d)


for y in range(1, H):
    x = 0
    d = abs(dist_map[y][x])
    dp[y][x] = (dp[y - 1][x] << d) | (dp[y - 1][x] >> d)


for y in range(1, H):
    for x in range(1, W):
        d = abs(dist_map[y][x])
        dp[y][x] = (dp[y][x - 1] << d) | (dp[y][x - 1] >> d) | ((dp[y - 1][x] << d) | (dp[y - 1][x] >> d))


ans = dp[-1][-1]

for i in range(mid + 1):
    if (ans & (1 << (mid - i))) or (ans & (1 << (mid + i))):
        print(i)
        return
