h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [list(map(int, input().split())) for i in range(h)]

ab = [[0] * w for i in range(h)]
for ch in range(h):
    for cw in range(w):
        ab[ch][cw] = abs(a[ch][cw] - b[ch][cw])

ab0 = ab[0][0]
size = 80 * (h + w)
dp = [[0] * w for hh in range(h)]
dp[0][0] |= 2**(size + ab0)
dp[0][0] |= 2**(size - ab0)
for ch in range(h):
    for cw in range(w):
        if ch < h - 1:
            dp[ch + 1][cw] |= dp[ch][cw] << ab[ch + 1][cw]
            dp[ch + 1][cw] |= dp[ch][cw] >> ab[ch + 1][cw]
        if cw < w - 1:
            dp[ch][cw + 1] |= dp[ch][cw] << ab[ch][cw + 1]
            dp[ch][cw + 1] |= dp[ch][cw] >> ab[ch][cw + 1]

a = dp[h - 1][w - 1] >> size
m = a & (-a)
print(m.bit_length() - 1)
