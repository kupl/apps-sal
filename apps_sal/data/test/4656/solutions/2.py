from math import *


def r1(t):
    return t(input())


def r2(t):
    return [t(i) for i in input().split()]


def r3(t):
    return [t(i) for i in input()]


for _ in range(r1(int)):
    n, k = r2(int)
    s = r1(str)
    mp = {}
    for i in s:
        mp[i] = 0
    for i in s:
        mp[i] += 1

    t = sorted(list(mp.values()), reverse=True)
    ans = 1
    for x in range(1, k + 1):
        if k % x == 0:
            y = 1
            while True:
                ta = 0
                for i in t:
                    ta += i // y
                if (ta < x):
                    break
                ans = max(ans, y * x)
                y += 1

    print(ans)
