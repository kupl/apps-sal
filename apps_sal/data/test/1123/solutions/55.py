n,k=list(map(int,input().split()))
m=1000000007
ans=0
dp=[0]*(k+1) #dp[i]:=iを数列内の最大値とするもののgcd合計
for i in range(k,0,-1):
  mul_i=k//i#iの倍数の個数
  dp[i]=pow(mul_i,n,m)
  for j in range(2,mul_i+1):
    dp[i]=(m+dp[i]-dp[i*j])%m
  ans+=i*dp[i]%m
ans%=m
print(ans)





