maxV = 80 * (80 + 80)

H, W = list(map(int, input().split()))
Ass = [tuple(map(int, input().split())) for _ in range(H)]
Bss = [tuple(map(int, input().split())) for _ in range(H)]

dp = [[0 for j in range(W)] for i in range(H)]

for i in range(H):
    for j in range(W):
        A, B = Ass[i][j], Bss[i][j]
        if A > B:
            A, B = B, A
        if i == 0 and j == 0:
            dp[i][j] = 1 << (maxV + B - A) | 1 << (maxV - B + A)
        if i > 0:
            dp[i][j] |= dp[i - 1][j] << (B - A) | dp[i - 1][j] >> (B - A)
        if j > 0:
            dp[i][j] |= dp[i][j - 1] << (B - A) | dp[i][j - 1] >> (B - A)

bitset = dp[-1][-1]
mask = 1 << (2 * maxV)
ans = maxV
for i in range(-maxV, maxV + 1):
    if bitset & mask:
        ans = min(ans, abs(i))
    mask >>= 1

print(ans)
