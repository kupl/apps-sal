import sys
import os
if 'local' in os.environ:
    sys.stdin = open('./input.txt', 'r')


def f():
    return list(map(int, input().split()))


def midigit(x):
    return str(x)


def solve():
    t = f()[0]
    for _ in range(t):
        (a, k) = f()
        if k == 1:
            print(a)
            continue
        for i in range(k - 1):
            an = a + int(min(str(a))) * int(max(str(a)))
            if a == an:
                break
            a = an
        print(a)


solve()
