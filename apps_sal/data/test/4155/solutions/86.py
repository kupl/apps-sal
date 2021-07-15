n=int(input())
a=list(map(int,input().split()))
b=[0 for _ in range(n)]

ans=0

while a!=b:
  ch=0
  for i in range(n):
    if b[i]+1<=a[i]:
      b[i]+=1
      ch+=1
    elif b[i]+1>a[i] and ch>0:
      ch=0
      ans+=1
      
    if ch>0 and i==n-1:
      ans+=1
      
print(ans)

