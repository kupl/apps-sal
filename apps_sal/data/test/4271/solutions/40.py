n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
ans=0
for i in range(len(a)):
  ai=a[i]
  ans+=b[ai-1]
  if(ans!=b[ai-1]):
    if(ai==before+1):
      ans+=c[before-1]
  before=ai
print(ans)
