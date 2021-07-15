import sys
n,k=map(int,input().split())
x=list(map(int,input().split()))
left=[]
right=[]
origin=0
for u in x:
  if u<0:
    left.append(abs(u))
  elif u==0:
    origin+=1
  else:
    right.append(u)
left.sort()
k-=origin
if k==0:
  print(0)
  return
r=len(right)
l=len(left)
ans=float('inf')
if k<=r:
  ans=right[k-1]
if k<=l:
  ans=min(ans,left[k-1])
for i in range(k-1):
  if i<r and k-i-2<l:
    y=right[i]+left[k-i-2]+min(right[i],left[k-i-2])
    ans=min(ans,y)
print(ans)
