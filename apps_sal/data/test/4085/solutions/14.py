Q = int(input())

def decompose(x):
  ans = {}
  cx = x
  d = 2
  while d * d <= cx:
    t = 0
    while x % d == 0:
      t += 1
      x = x // d
    if t > 0:
      ans[d] = t
    d += 1
  if x > 1:
    ans[x] = 1
  return ans

def fastpow(x, p):
  if p == 0:
    return 1
  ans = fastpow(x, p // 2)
  ans *= ans
  if p % 2 == 1:
    ans *= x
  return ans

def makePrimePower(divs):
  primePowers = {}
  for d in divs:
    ppows = decompose(d)
    for key in ppows:
      if key not in primePowers:
        primePowers[key] = ppows[key]
      else:
        primePowers[key] = max(primePowers[key], ppows[key])
  return primePowers

def solve(divs):
  primePowers = makePrimePower(divs)
  x = 1
  for key in primePowers:
    x *= fastpow(key, primePowers[key])
  if x in divs:
    prim = list(primePowers.keys())[0]
    x *= prim
    primePowers[prim] += 1
  nrdivs = 1
  for key in primePowers:
    nrdivs *= primePowers[key] + 1
  if len(divs) + 2 != nrdivs:
    return -1
  return x

for x in range(Q):
  N = int(input())
  divs = list(map(int, input().split()))
  print(solve(divs))

