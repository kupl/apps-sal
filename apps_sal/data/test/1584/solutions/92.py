N=int(input())
l=list(map(int,input().split()))
l.sort()
import bisect
ans=0
for i in range(N):
   for j in range(i+1,N):
      ans+=bisect.bisect_left(l,l[i]+l[j])-j-1
print(ans)
