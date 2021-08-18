import math
import sys


def chek(m, b, c, li):
    for i in range(li):
        if m[i] + b[i] > c:
            return False
    return True


def input(): return sys.stdin.readline().rstrip()


f = int(input())
for _ in range(f):
    n = int(input())
    n = n * 4
    for i in range(n, n // 2, -1):
        if i % 2 == 0:
            print(i, end=' ')
    print()
