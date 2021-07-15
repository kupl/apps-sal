H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
B = [list(map(int,input().split())) for i in range(H)]
C = [[abs(a-b) for a,b in zip(arow,brow)] for arow,brow in zip(A,B)]

ofs = 80*(H+W)
dp = [[0]*W for _ in range(H)]
dp[0][0] = (1<<(ofs+C[0][0])) | (1<<(ofs-C[0][0]))
for i,crow in enumerate(C):
    for j,c in enumerate(crow):
        if i:
            dp[i][j] = (dp[i-1][j]<<c) | (dp[i-1][j]>>c)
        if j:
            dp[i][j] |= ((dp[i][j-1]<<c) | (dp[i][j-1]>>c))

ans = ofs*2
for i in range(ofs*2):
    if dp[-1][-1]&(1<<i):
        ans = min(ans, abs(i-ofs))
print(ans)
