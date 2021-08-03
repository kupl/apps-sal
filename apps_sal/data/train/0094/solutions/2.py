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


t = II()
for q in range(t):
    n, k = MI()
    a = LI()
    d = [0] * n
    c = a.count(k // 2)
    boo = k % 2 == 0
    count = 0
    for i in range(n):
        if a[i] < k // 2:
            d[i] = 0
        elif a[i] == k // 2:
            if not boo:
                d[i] = 0
            elif count < c // 2:
                d[i] = 0
                count += 1
            else:
                d[i] = 1
        else:
            d[i] = 1
    print(*d)
