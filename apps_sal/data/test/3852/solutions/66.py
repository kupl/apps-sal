n=int(input())
a=list(map(int,input().split()))
mxn=0
mnn=0
mx=-10**10
mn=10**10
for i in range(n):
  if mx<a[i]:
    mx=a[i]
    mxn=i
  if mn>a[i]:
    mn=a[i]
    mnn=i
print(2*n-1)
if mx+mn>=0:
  for i in range(n):
    print(mxn+1,i+1)
  for i in range(1,n):
    print(i,i+1)
else:
  for i in range(n):
    print(mnn+1,i+1)
  for i in range(n,1,-1):
    print(i,i-1)
