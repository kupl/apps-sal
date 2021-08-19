#
# Written by NoKnowledgeGG @YlePhan
# ('ω')
#
#import math
#mod = 10**9+7
#import itertools
#import fractions
#import numpy as np
#mod = 10**4 + 7
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
  if b == 0:#結局はc,0の最大公約数はcなのに
    return a
  return gcd_(a,a % b) # a = p * b + q"""
"""def extgcd(a,b,x,y):
  d = a
  if b!=0:
    d = extgcd(b,a%b,y,x)
    y -= (a//b) * x
    print(x,y)
  else:
    x = 1
    y = 0
  return d"""


def readInts():
    return list(map(int, input().split()))


def main():
    n, a = readInts()

    X = readInts()

    X = list(map(lambda i: i - a, X))  # lambda iに、 i - aという演算のもと Xから入れる
    # ここで、平均が8になるもの key = 0の時が答えになる。
    # だからこそ　答えで dp[0] - 1 するのはこのため

    dp = {0: 1}

    for i in X:
        for k, v in list(dp.items()):  # key,valueをそれぞれ抽出
            dp[i + k] = dp.get(i + k, 0) + v
            #
            # get(なんか) なんかに入ってる辞書のvalueが返ってくる
            # 無かったら、get(なんか,〇)で、〇に入ってるので辞書が更新される
            #
    # print(dp)
    #{0: 6, 1: 6, 2: 2, -1: 2}
    # 負の数にも対応している
    print(dp[0] - 1)


def __starting_point():
    main()


__starting_point()
