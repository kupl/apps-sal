import math        # factorical（階乗) # hypot(距離)
# import heapq
# from fractions import gcd # Python3.5以前 # lcm（最小公倍数） = (a*b)//gcd(a,b)
# from fractions import Fraction
# from math import gcd # Python3.6以降
# --------------------------------------------------------------

# 素因数,個数 の組リストを出力


def fctr1(n):
    f = []
    c = 0
    r = int(n**0.5)
    for i in range(2, r + 2):
        while n % i == 0:
            c += 1
            n = n // i
        if c != 0:
            f.append([i, c])
            c = 0
    if n != 1:
        f.append([n, 1])
    return f


a, b = map(int, input().split())

print(len(fctr1(math.gcd(a, b))) + 1)
