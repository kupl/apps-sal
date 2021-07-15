N=input()
DP=[[0]*(len(N)+1) for i in range(4)]
DP[0][0]=1#後側が位置
mod=10**9+7
for i in range(len(N)):
   if N[i]=="A":
      DP[0][i+1]=DP[0][i]%mod
      DP[1][i+1]=(DP[1][i]+DP[0][i])%mod
      DP[2][i+1]=DP[2][i]%mod
      DP[3][i+1]=DP[3][i]%mod
   elif N[i]=="B":
      DP[0][i+1]=DP[0][i]%mod
      DP[1][i+1]=DP[1][i]%mod
      DP[2][i+1]=(DP[2][i]+DP[1][i])%mod
      DP[3][i+1]=DP[3][i]%mod
   elif N[i]=="C":
      DP[0][i+1]=DP[0][i]%mod
      DP[1][i+1]=DP[1][i]%mod
      DP[2][i+1]=DP[2][i]%mod
      DP[3][i+1]=(DP[3][i]+DP[2][i])%mod
   else:
      DP[3][i+1]=(3*DP[3][i]+DP[2][i])%mod
      DP[0][i+1]=(DP[0][i]*3)%mod
      DP[1][i+1]=(DP[1][i]*3+DP[0][i])%mod
      DP[2][i+1]=(DP[2][i]*3+DP[1][i])%mod
print(DP[3][-1]%mod)
