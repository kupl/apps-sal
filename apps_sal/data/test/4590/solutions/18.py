n,m,k=map(int,input().split())
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

acum1=[0]
for i in range(n):
  acum1.append(acum1[-1]+arr1[i])
acum2=[0]
for i in range(m):
  acum2.append(acum2[-1]+arr2[i])
ans=0
j=m
for i in range(n+1):
  if acum1[i]>k:
    break
  while acum2[j]>k-acum1[i] and j>0:
    j-=1
  ans=max(ans,i+j)
print(ans)
