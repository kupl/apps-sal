def sumab(a, b):
  return (a+b)*(b-a+1)//2
def calc(spot, H):
  if spot <= H:	return spot * (spot + 1) // 2
  if (H - spot) % 2 == 0: return sumab(1,H+(spot-H)//2)+sumab(H,H+(spot-H)//2-1)
  return sumab(1,H+(spot-H)//2)+sumab(H,H+(spot-H)//2-1)+H+(spot-H)//2



def solve():
  n,H = map(int,input().split())
  if n == 1:
    print(1)
    return 0
  st = 1
  en = 10**20
  while st < en:
    mid = (st+en)//2
    if calc(mid,H) >= n:
      en = mid
    else:
      st = mid+1
  print(st)
solve()
