import math
import collections


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


(x, k, d) = mi()
x = abs(x)
count = min(k, x // d)
k -= count
x -= d * count
if k % 2 == 0:
    print(x)
else:
    print(d - x)
