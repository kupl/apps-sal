import sys


def rint():
    return list(map(int, sys.stdin.readline().split()))


def input():
    return sys.stdin.readline().rstrip('\n')


def oint():
    return int(input())


q = oint()
for _ in range(q):
    n = oint()
    odd = 0
    ss = ''
    for _ in range(n):
        s = input()
        ss = ss + s
        if len(s) % 2:
            odd = 1
    if odd:
        print(n)
    elif ss.count('1') % 2:
        print(n - 1)
    else:
        print(n)
