from functools import lru_cache
import sys
sys.setrecursionlimit(10 ** 8)
h,n=map(int,input().split())
ab=[tuple(map(int,input().split())) for _ in range(n)]
ab.sort(key=lambda abi:(abi[1]/abi[0],abi[0]))

@lru_cache(maxsize=None)
def dp(i):
  if i<=0:
    return 0
  else:
    ans=float('inf')
    for a,b in ab:
      val=b+dp(i-a)
      if val<ans:
        ans=val
      else:
        break
    return ans

print(dp(h))
