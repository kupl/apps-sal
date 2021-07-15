N=int(input())
A=list(map(int,input().split()))

A.sort()

dp=[False]*(10**6*2)
ans=0
for idx,i in enumerate(A):
  if dp[i]:continue
  tmp=i
  ans+=1
  while tmp<10**6*2-1:
    dp[tmp]=True
    tmp+=i
  if idx!=len(A)-1 and A[idx+1]==i:
    ans-=1
print(ans)
