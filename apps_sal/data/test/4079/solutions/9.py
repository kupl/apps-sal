import math


def na():
    n = int(input())
    b = [int(x) for x in input().split()]
    return n, b


def nab():
    n = int(input())
    b = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]
    return n, b, c


def dv():
    n, m = list(map(int, input().split()))
    return n, m


def dva():
    n, m = list(map(int, input().split()))
    b = [int(x) for x in input().split()]
    return n, m, b


def nm():
    n = int(input())
    b = [int(x) for x in input().split()]
    m = int(input())
    c = [int(x) for x in input().split()]
    return n, b, m, c


def dvs():
    n = int(input())
    m = int(input())
    return n, m


n = int(input())
for i in range(n):
    s = input()
    if len(s) == 1:
        print('Yes')
        continue
    if len(set(s)) < len(s):
        print('No')
        continue
    s = sorted(set(s))
    f = True
    for i in range(len(s) - 1):
        d = ord(s[i])
        d1 = ord(s[i + 1])
        if d1 - d != 1:
            print('No')
            f = False
            break
    if f:
        print('Yes')
