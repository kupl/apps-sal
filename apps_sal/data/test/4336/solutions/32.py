import math
import collections


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


(w, h, x, y) = mi()
ans = w * h / 2
check = 0
if x == w / 2 and y == h / 2:
    check = 1
print('{} {}'.format(ans, check))
