"""
    Auther: ghoshashis545 Ashis Ghosh
    college: jalpaiguri Govt Enggineering College
    Date:07/03/2020
"""
from math import ceil, sqrt, gcd, log, floor
from collections import deque


def ii():
    return int(input())


def si():
    return input()


def mi():
    return map(int, input().strip().split(' '))


def li():
    return list(mi())


for _ in range(ii()):
    n = ii()
    a = li()
    f = 0
    for i in range(n):
        if a[i] % 2 == 0:
            print('1')
            print(i + 1)
            f = 1
            break
    if f == 0:
        if n == 1:
            print('-1')
        else:
            print('2')
            print(1, 2)
