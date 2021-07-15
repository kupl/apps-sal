x, k = map(int, input().split())

mod = 10**9+7

def bp(n,p):
  if p == 0:
    return 1
  elif p % 2 == 0:
    return bp(n**2 % mod, p // 2)
  else:
    return (bp(n**2 % mod, p // 2) * n) % mod

def f(n,x):
  return (bp(2,n) * x - bp(2,n) + 1) % mod

if x > 0:
  print(f(k,2*x) % mod)
else:
  print(0)
