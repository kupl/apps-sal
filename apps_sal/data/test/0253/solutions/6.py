from math import gcd
import sys


def f():
    a, b, c = sorted(map(int, input().split()))

    x1 = 0
    for x2 in range(100):
        for x3 in range(100):
            ok = True
            for t in range(x3, x3 + 5000):
                if (t - x1) % a == 0 or (t - x2) % b == 0 or (t - x3) % c == 0:
                    continue
                else:
                    ok = False
                    break
            if ok:
                print('YES')
                return
    print('NO')


f()
