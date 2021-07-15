import bisect
n=int(input())
l=list(map(int,input().split()))
l.sort()
ans=0
for i in range(n-2):
  for j in range(i+1,n-1):
    res=l[i]+l[j]
    mid=bisect.bisect_left(l,res)
    ans+=mid-j-1
print(ans)
