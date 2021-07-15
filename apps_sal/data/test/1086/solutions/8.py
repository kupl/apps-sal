# Atcoder Problem Solving
H,W=map(int,input().split())
c=[list(map(int,input().split())) for i in range(H)]
b=[list(map(int,input().split())) for i in range(H)]
a=[[0 for i  in range(W)] for j in range(H)]

for i in range(H):
    for j in range(W):
        a[i][j]=abs(c[i][j]-b[i][j])
        
dp=[[0 for i in range(W)] for j in range(H)]

# Bitset演算
# 答えは絶対値が絶対-80から80以内に収まる

X=3200

dp[0][0]= (1<<(X+a[0][0]))  | (1<<(X-a[0][0]))
# 初期化の条件

for i in range(H):
    for j in range(W):
        if 0<=i<H and 0<=j+1<W:
            dp[i][j+1]|=(dp[i][j]<<a[i][j+1])
            dp[i][j+1]|=(dp[i][j]>>a[i][j+1]) 
            
        if 0<=i+1<H and 0<=j<W:
            dp[i+1][j]|=(dp[i][j]<<a[i+1][j])
            dp[i+1][j]|=(dp[i][j]>>a[i+1][j])
            
A=str(bin(dp[H-1][W-1]))[::-1]
L=len(A)
ans=3200
for i in range(L):
    if A[i]=="1":
        ans=min(ans,abs(i-X))
print(ans)
