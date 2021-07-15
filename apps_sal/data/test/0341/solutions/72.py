n,k = list(map(int,input().split()))
r,s,p = list(map(int,input().split()))
T = input()

#dp[i][j]:i回目にjを出した時のそれまでの合計点の最大値。j:0グー1チョキ2パー
dp = [[0 for j in range(3)] for i in range(n)]
for i in range(0,k):
    if T[i] == 'r':
        dp[i][2] = p 
    elif T[i] == 's':
        dp[i][0] = r 
    else:
        dp[i][1] = s 
    for j in range(k,n-i,k):
        if T[i+j] == 'r':
            dp[i+j][2] = max(dp[i+j-k][0]+p,dp[i+j-k][1]+p)
            dp[i+j][1] = max(dp[i+j-k][0],dp[i+j-k][2])
            dp[i+j][0] = max(dp[i+j-k][1],dp[i+j-k][2])
        elif T[i+j] == 's':
            dp[i+j][0] = max(dp[i+j-k][1]+r,dp[i+j-k][2]+r)
            dp[i+j][1] = max(dp[i+j-k][0],dp[i+j-k][2])
            dp[i+j][2] = max(dp[i+j-k][0],dp[i+j-k][1])
        else:
            dp[i+j][1] = max(dp[i+j-k][2]+s,dp[i+j-k][0]+s)
            dp[i+j][0] = max(dp[i+j-k][1],dp[i+j-k][2])
            dp[i+j][2] = max(dp[i+j-k][0],dp[i+j-k][1])
    
total = 0
#print(dp)
for i in range(n-1,max(0,n-1-k),-1):
    total += max(dp[i])
print(total)
        
    


