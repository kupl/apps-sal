import sys
input = sys.stdin.readline

H, W = list(map(int, input().split()))
A = [list(map(int, input().split())) for i in range(H)]
B = [list(map(int, input().split())) for i in range(H)]
D = [[0]*W for i in range(H)]
for i in range(H):
    for j in range(W):
        D[i][j] = abs(A[i][j]-B[i][j])
buf = 80*(H+W)
dp = [[0]*W for i in range(H)]
dp[0][0] = 1<<(buf+D[0][0]) | 1<<(buf-D[0][0])
for i in range(H):
    for j in range(W):
        d = D[i][j]
        if i:
            dp[i][j] |= dp[i-1][j]<<d | dp[i-1][j]>>d
        if j:
            dp[i][j] |= dp[i][j-1]<<d | dp[i][j-1]>>d
ans = 10**18
for i in range(buf*2+1):
    if dp[H-1][W-1]&(1<<i):
        ans = min(ans, abs(buf-i))
print(ans)

