H, W = map(int, input().split())
A = [[0] * W for i in range(H)]
B = [[0] * W for i in range(H)]
for i in range(H):
    inf = [int(c) for c in input().split()]
    for j in range(W):
        A[i][j] = inf[j]

for i in range(H):
    inf = [int(c) for c in input().split()]
    for j in range(W):
        B[i][j] = inf[j]

X = (H + W) * 80
dp = [[0] * W for i in range(H)]
d = abs(A[0][0] - B[0][0])
dp[0][0] = 1 << (X + d)

for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            continue
        d = abs(A[i][j] - B[i][j])
        if i != 0:
            dp[i][j] |= dp[i - 1][j] >> d
            dp[i][j] |= dp[i - 1][j] << d
        if j != 0:
            dp[i][j] |= dp[i][j - 1] >> d
            dp[i][j] |= dp[i][j - 1] << d

s = bin(dp[-1][-1])[2:]
l = len(s) - 1
ans = float('inf')
for i in range(l, -1, -1):
    if s[i] == '1':
        m = abs(l - i - X)
        if m < ans:
            ans = m
print(ans)
