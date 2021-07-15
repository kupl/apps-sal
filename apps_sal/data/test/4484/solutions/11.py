n, m = [int(x) for x in input().split()]
mod = 10 ** 9 + 7

def kaizyou(p):
  ans = 1
  for i in range(1,p+1):
    ans *= i
    if ans >= mod:
      ans %= mod
  return ans
  
res = 0
if abs(m - n) <= 1:
  res += kaizyou(m)
  res %= mod
  res *= kaizyou(n)
  res %= mod
  if n == m:
    res *= 2
  res %= mod

print(res)
