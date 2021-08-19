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
    ans = ''
    for i in range(0, len(s), 2):
        ans += s[i]
    print(ans + s[-1])
