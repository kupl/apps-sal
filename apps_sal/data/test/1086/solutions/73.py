import sys


def input():
    return sys.stdin.readline().rstrip()


sys.setrecursionlimit(10 ** 7)
(H, W) = map(int, input().split())
A = [[int(x) for x in input().split()] for _ in range(H)]
B = [[int(x) for x in input().split()] for _ in range(H)]
C = [[0] * W for _ in range(H)]
for i in range(H):
    for j in range(W):
        C[i][j] = abs(A[i][j] - B[i][j])
center = 80 * (H + W)
dp = [[0] * W for _ in range(H)]
dp[0][0] = 1 << center - C[0][0] | 1 << center + C[0][0]
for i in range(H):
    for j in range(W):
        if i:
            dp[i][j] |= dp[i - 1][j] << C[i][j]
            dp[i][j] |= dp[i - 1][j] >> C[i][j]
        if j:
            dp[i][j] |= dp[i][j - 1] << C[i][j]
            dp[i][j] |= dp[i][j - 1] >> C[i][j]
ans = center * 2
for i in range(center * 2):
    if dp[H - 1][W - 1] >> i & 1:
        ans = min(ans, abs(i - center))
print(ans)
