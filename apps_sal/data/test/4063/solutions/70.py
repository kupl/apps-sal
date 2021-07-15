from bisect import bisect_left

n=int(input())
d=list(map(int,input().split()))
d=sorted(d)
ans=0

for i in range(1,10**5+1):
  p=bisect_left(d,i)
  ans+=1 if p==(n-p) else 0

print(ans)
