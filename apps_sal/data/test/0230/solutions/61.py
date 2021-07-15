import sys
sys.setrecursionlimit(10**9)
from collections import defaultdict
N = int(input())
S = input()
if N==2:
  if S[1] == S[0]:
    print((1))
  else:
    print((0))
  return
def hantei(mid):
  flag = False
  string = S[:mid]
  dic = defaultdict(int)
  dic[string] = -1
  for k in range(mid, N):
    string += S[k]
    string = string[1:]
    if dic[string] < 0:
      if k -mid+2+ dic[string] >= mid:
        flag = True
        break
    else:
      dic[string] = -k+mid-2
  if flag:
    return True
  else: 
    return False
ok = N//2+1 #False
ng = 0 #True
while ok - ng > 1:
  mid = (ok + ng) // 2
  if hantei(mid):
    ng = mid
  else:
    ok = mid
if hantei(mid):
  print((min(mid, N//2)))
else:
  print((min(ng, N//2)))

