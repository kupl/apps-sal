n,m=map(int,input().split())
a=list(map(int,input().split()))
table={
  1:2,
  2:5,
  3:5,
  4:4,
  5:5,
  6:6,
  7:3,
  8:7,
  9:6,
}
dp=[-1]*(n+1)
dp[0]=0
for i in range(1,n+1):
  mx=-1
  for j in a:
    if not 0 <= i-table[j] < n+1:
      continue
    #print(i,i-table[j],dp[i-table[j]],j)
    if dp[i-table[j]]<0:
      continue
    if mx < dp[i-table[j]]*10+j:
      mx =dp[i-table[j]]*10+j
  dp[i]=mx
print(dp[n])
