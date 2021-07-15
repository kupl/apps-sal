import sys
readline = sys.stdin.readline

N = int(readline())

ok = 0
ng = 10 ** 18 + 1

def isOk(x):
  if (1 + x) * x // 2 <= N + 1:
    return True
  return False
  
while abs(ng - ok) > 1:
  mid = abs(ng + ok) // 2
  if isOk(mid):
    ok = mid
  else:
    ng = mid

print(N + 1 - ok)
