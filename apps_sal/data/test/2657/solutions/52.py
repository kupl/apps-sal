n=int(input())
a=list(map(int,input().split()))
a.sort()
b=a[-1]/2
tmp=a[-1]
for i in range(n):
  if tmp>abs(b-a[i]):
    ans=a[i]
    tmp=abs(b-a[i])
print(a[-1],ans)
