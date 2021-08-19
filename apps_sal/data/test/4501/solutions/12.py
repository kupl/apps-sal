def kiri(n, m):
    r_ = n / m
    if r_ - n // m > 0:
        return n // m + 1
    else:
        return n // m


' n! mod m 階乗\nmod = 1e9 + 7\nN = 10000000\nfac = [0] * N\ndef ini():\n  fac[0] = 1 % mod\n  for i in range(1,N):\n    fac[i] = fac[i-1] * i % mod'
'mod = 1e9+7\nN = 10000000\npw = [0] * N\ndef ini(c):\n  pw[0] = 1 % mod\n  for i in range(1,N):\n    pw[i] = pw[i-1] * c % mod'
"\ndef YEILD():\n  yield 'one'\n  yield 'two'\n  yield 'three'\ngenerator = YEILD()\nprint(next(generator))\nprint(next(generator))\nprint(next(generator))\n"
'def gcd_(a,b):\n  if b == 0:#結局はc,0の最大公約数はcなのに\n    return a\n  return gcd_(a,a % b) # a = p * b + q'
'def extgcd(a,b,x,y):\n  d = a\n  if b!=0:\n    d = extgcd(b,a%b,y,x)\n    y -= (a//b) * x\n    print(x,y)\n  else:\n    x = 1\n    y = 0\n  return d'


def readInts():
    return list(map(int, input().split()))


def main():
    (n, a) = readInts()
    X = readInts()
    X = list(map(lambda i: i - a, X))
    dp = {0: 1}
    for i in X:
        for (k, v) in list(dp.items()):
            dp[i + k] = dp.get(i + k, 0) + v
    print(dp[0] - 1)


def __starting_point():
    main()


__starting_point()
