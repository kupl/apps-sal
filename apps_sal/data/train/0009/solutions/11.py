import sys
import math


def II():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def MI():
    return map(int, sys.stdin.readline().split())


def SI():
    return sys.stdin.readline().strip()


t = II()
for q in range(t):
    s = SI()
    a = []
    count = 0
    for i in range(len(s)):
        if s[i] == "1":
            count += 1
        else:
            a.append(count)
            count = 0
    a.append(count)
    a.sort(reverse=True)
    print(sum(a[0:len(a):2]))
