import numpy as np
H, W = list(map(int, input().split()))
A = np.array([list(map(int, input().split())) for _ in range(H)])
B = np.array([list(map(int, input().split())) for _ in range(H)])

C = abs(A - B)
# print (C)

D = 80 * (H + W + 1) + 10
D2 = D * 2

dp = [[0] * (W) for _ in range(H)]

dp[0][0] = 1 << (D - int(C[0][0]))
# print (dp[0][0])
dp[0][0] |= 1 << (D + int(C[0][0]))
# print ((dp[0][0]))



# print (dp[0][0])
dp = np.array(dp)

for h in range(H):
    for w in range(W):
        tmp = int(C[h][w])
        if h:
            dp[h][w] |= dp[h - 1][w] << tmp
            dp[h][w] |= dp[h - 1][w] >> tmp
        if w:
            dp[h][w] |= dp[h][w - 1] << tmp
            dp[h][w] |= dp[h][w - 1] >> tmp

        
ans = D2
# print (ans)
tmp = dp[H - 1][W - 1]
for i in range(D2):
    if (tmp >> i) & 1:
        ans = min(ans, abs(i - D))

print (ans)


