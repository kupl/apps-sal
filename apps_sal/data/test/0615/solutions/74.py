n=int(input())
a=list(map(int,input().split()))
score=[a[0],0,a[1]+a[2],sum(a[3:])]
ans=10**18
i,k=1,3
for j in range(2,n-1):
  score[1]+=a[j-1]
  score[2]-=a[j-1]
  while abs(score[0]-score[1])>abs(score[0]+a[i]-score[1]+a[i]):
    score[0]+=a[i]
    score[1]-=a[i]
    i+=1
  while abs(score[2]-score[3])>abs(score[2]+a[k]-score[3]+a[k]):
    score[2]+=a[k]
    score[3]-=a[k]
    k+=1
  ans=min(ans,max(score)-min(score))
print(ans)
