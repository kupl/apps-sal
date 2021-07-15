from math import *
def fct(n):

  res = []
  sqfree = 1
  for p in range(2, int(sqrt(n) + 10)):
    cnt = 0
    while n % p == 0:
      cnt += 1
      n //= p
    if cnt > 0:
      res.append(cnt)
      sqfree *= p

  if n != 1:
    res.append(1)
    sqfree *= n
  return res, sqfree

def solve(n):
  if n == 1: return (1, 0)
  fctr, sqfree = fct(n)
  # print("fctr = ", fctr)
  mx = max(fctr)
  # print("mx = ", mx)
  next_pow2 = 2**ceil(log(mx)/log(2))

  # print("next_pow2  = ", next_pow2)
  times = 0
  if (any(x != next_pow2 for x in fctr)):
    times += 1

  while next_pow2 != 1:
    next_pow2 //= 2
    times += 1

  return sqfree, times

print(*solve(int(input())))

