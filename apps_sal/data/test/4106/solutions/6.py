from sys import stdin, stdout
import collections

#T = int(input())
#s = input()
N,K,X = [int(x) for x in stdin.readline().split()]
arr = [int(x) for x in stdin.readline().split()]

if X < N//K:
    print(-1)
    quit()
    
dp = [[0]*N for _ in range(X)]

for i in range(K):
    dp[0][i] = arr[i]
    
for i in range(X-1):
    for j in range(N):
        if dp[i][j]!=0:
            for z in range(j+1,min(j+K+1,N)):
                #print(i,j,i+1,z)
                dp[i+1][z] = max(dp[i+1][z], dp[i][j] + arr[z])
                

res = 0        
for i in range(N-K,N):
    res = max(res,dp[X-1][i])
    
print(res)
