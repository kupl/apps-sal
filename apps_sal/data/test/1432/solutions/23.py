n=int(input())
a=list(map(int,input().split()))
ans=[0]*n
ans[0]=sum([2*a[i] for i in range(1,n,2)])
ans[0]=sum(a)-ans[0]

for i in range(n-1):
  ans[i+1]=2*a[i]-ans[i]

print((*ans))

