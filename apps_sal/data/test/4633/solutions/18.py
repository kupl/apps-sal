import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return list(map(int, sys.stdin.readline().split()))


def SI():
    return sys.stdin.readline().strip()


def findSum(n, s):
    su = 0
    ind = -1
    for i in range(len(n)):
        su += int(n[i])
        if su > s:
            ind = i
            break
    return ind


t = II()
for q in range(t):
    (n, s) = MI()
    n = str(n)
    ans = 0
    ind = findSum(n, s)
    while ind != -1:
        f = n[:ind]
        if f == '':
            f = '0'
        se = '0' + '0' * (len(n) - ind - 1)
        f = str(int(f) + 1) + se
        ans += int(f) - int(n)
        n = f
        ind = findSum(n, s)
    print(ans)
