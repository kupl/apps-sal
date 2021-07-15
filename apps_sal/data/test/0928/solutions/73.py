n,k=list(map(int,input().split()))
a=list(map(int,input().split()))
from itertools import accumulate
from bisect import bisect_left
a=[0]+list(accumulate(a))



ans=0
#区間の端を決めてあるところでkを越えればそれから先はずっと超える
for i in range(n+1):
  j=bisect_left(a,k+a[i])
  ans=ans+n-j+1
print(ans)

  

