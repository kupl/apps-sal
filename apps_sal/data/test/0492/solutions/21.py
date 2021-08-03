#!/usr/bin/env python3
from sys import stdin, stdout


def rint():
    return list(map(int, stdin.readline().split()))
#lines = stdin.readlines()


t = {'v': 0, '<': 1, '^': 2, '>': 3}

a, b = list(map(str, input().split()))
n = int(input())
n %= 4
if n == 0 or n == 2:
    print('undefined')
    return
a, b = t[a], t[b]
if b < a:
    b += 4

diff = b - a
if n == 1:
    if diff == 1:
        print("cw")
    elif diff == 3:
        print("ccw")
    else:
        print('undefined')
elif n == 3:
    if diff == 1:
        print("ccw")
    elif diff == 3:
        print("cw")
    else:
        print('undefined')
