from bisect import *
def solve():
  ans = 0
  N, D, A = list(map(int, input().split()))
  B = [list(map(int, input().split())) for _ in range(N)]
  B.sort()
  lasts = [0]*(N+1)
  now = 0
  for i,((x,h),l) in enumerate(zip(B,lasts)):
    now -= l
    atack = max(0,-(-(h-now)//A))
    ans += atack
    damage = atack*A
    now += damage
    last = x+2*D
    ind = bisect_right(B,[last+1,0])
    lasts[ind] += damage
  return ans
print((solve()))

