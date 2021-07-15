N,M=map(int,input().split())
num={1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
A=list(map(int,input().split()))
A.sort(reverse = True)
dp = [0]+[-1]*(N+1)
for i in range(N):
    for j in A:
        if i+num[j]<=N:
            dp[i+num[j]] = max(dp[i+num[j]],dp[i]+1)
ans = []
m=N
while m>0:
    for i in A:
        if m-num[i]>=0 and dp[m-num[i]]==dp[m]-1:
          m-=num[i]
          ans.append(str(i))
          break
print("".join(ans))
