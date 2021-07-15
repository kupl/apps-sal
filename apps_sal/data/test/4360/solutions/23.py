n=int(input())
a=list(map(int,input().split()))
ans=0.0
for i in range(n):
  ans=ans+1.0/a[i]
ans=1.0/ans
print(ans)
