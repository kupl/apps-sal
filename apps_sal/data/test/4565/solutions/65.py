n=int(input())
S=list(input())
W=[0]*(n+1)
E=[0]*(n+1)
for i in range(n):
  W[i]=W[i-1]+S[i].count("W")
  E[n-i-1]=E[n-i]+S[n-i-1].count("E")
W = W[:n]
E = E[:n]
ans = 1000000
for i in range(n):
  ans = min(ans,W[i]+E[i]-1)
print(ans)

