n=int(input())
a=sorted([int(x) for x in input().split()],reverse=True)
ans=0
for i in range(n-1):
  ans+=a[(i+1)//2]
print(ans)
