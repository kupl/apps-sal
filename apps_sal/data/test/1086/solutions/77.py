H, W = map(int, input().split())
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
C = []
for arow, brow in zip(A, B):
    C.append([abs(a - b) for a, b in zip(arow, brow)])

ofs = 80 * (H + W)
dp = [0] * W
dp[0] = (1 << (ofs + C[0][0])) | (1 << (ofs - C[0][0]))
for j in range(W - 1):
    dp[j + 1] = (dp[j] << C[0][j + 1]) | (dp[j] >> C[0][j + 1])

for i in range(1, H):
    dp2 = [0] * W
    for j in range(W):
        dp2[j] = (dp[j] << C[i][j]) | (dp[j] >> C[i][j])
        if j:
            dp2[j] |= (dp2[j - 1] << C[i][j]) | (dp2[j - 1] >> C[i][j])
    dp = dp2

ans = ofs * 2
for i in range(ofs * 2):
    if dp[-1] & (1 << i):
        ans = min(ans, abs(ofs - i))
print(ans)
