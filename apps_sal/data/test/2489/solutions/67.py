import math
n=int(input())
a=list(map(int,input().split()))
a.sort()
maxa=max(a)
arr=[0]*(maxa+1)
for i in a:
  if arr[i]==0:
    t=math.ceil((maxa+1)/i)
    for j in range(t):
      arr[i*j]+=1
  elif arr[i]==1:
    arr[i]=2
ans=0
for i in a:
  if arr[i]==1:
    ans+=1
print(ans)
