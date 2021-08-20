from functools import reduce
import math
import sys
import collections as cl
import bisect as bs
sys.setrecursionlimit(100000)
input = sys.stdin.readline
mod = 10 ** 9 + 7
Max = sys.maxsize


def l():
    return list(map(int, input().split()))


def m():
    return map(int, input().split())


def onem():
    return int(input())


def s(x):
    a = []
    if len(x) == 0:
        return []
    aa = x[0]
    su = 1
    for i in range(len(x) - 1):
        if aa != x[i + 1]:
            a.append([aa, su])
            aa = x[i + 1]
            su = 1
        else:
            su += 1
    a.append([aa, su])
    return a


def jo(x):
    return ' '.join(map(str, x))


def max2(x):
    return max(map(max, x))


def In(x, a):
    k = bs.bisect_left(a, x)
    if k != len(a) and a[k] == x:
        return True
    else:
        return False


def pow_k(x, n):
    ans = 1
    while n:
        if n % 2:
            ans *= x
        x *= x
        n >>= 1
    return ans


'\ndef nibu(x,n,r):\n    ll = 0\n    rr = r\n    while True:\n        mid = (ll+rr)//2\n\n    if rr == mid:\n        return ll\n    if (ここに評価入れる):\n        rr = mid\n    else:\n        ll = mid+1\n'


def gcd(*numbers):
    return reduce(math.gcd, numbers)


def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def lcm_base(x, y):
    return x * y // math.gcd(x, y)


def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)


def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)


n = onem()
ans = 1
for i in range(1, n + 1):
    ans = lcm(ans, i)
print(ans + 1)
