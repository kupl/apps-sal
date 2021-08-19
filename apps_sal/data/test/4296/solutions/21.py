import math
import collections


def ii():
    return int(input())


def mi():
    return map(int, input().split())


def li():
    return list(map(int, input().split()))


(a, b, c) = mi()
if a + b + c >= 22:
    print('bust')
else:
    print('win')
