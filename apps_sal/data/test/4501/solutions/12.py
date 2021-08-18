def kiri(n, m):
    r_ = n / m
    if (r_ - (n // m)) > 0:
        return (n // m) + 1
    else:
        return (n // m)


""" n! mod m 階乗
mod = 1e9 + 7
N = 10000000
fac = [0] * N
def ini():
  fac[0] = 1 % mod
  for i in range(1,N):
    fac[i] = fac[i-1] * i % mod"""

"""mod = 1e9+7
N = 10000000
pw = [0] * N
def ini(c):
  pw[0] = 1 % mod
  for i in range(1,N):
    pw[i] = pw[i-1] * c % mod"""

"""
def YEILD():
  yield 'one'
  yield 'two'
  yield 'three'
generator = YEILD()
print(next(generator))
print(next(generator))
print(next(generator))
"""
"""def gcd_(a,b):
  if b == 0:
    return a
  return gcd_(a,a % b)
"""def extgcd(a, b, x, y):
  d = a
  if b != 0:
    d = extgcd(b, a % b, y, x)
    y -= (a // b) * x
    print(x, y)
  else:
    x = 1
    y = 0
  return d"""


def readInts():
    return list(map(int, input().split()))


def main():
    n, a = readInts()

    X = readInts()

    X = list(map(lambda i: i - a, X))  

    dp = {0: 1}

    for i in X:
        for k, v in list(dp.items()):  
            dp[i + k] = dp.get(i + k, 0) + v
    print(dp[0] - 1)


def __starting_point():
    main()


__starting_point()
