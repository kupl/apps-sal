import re
import math
import decimal
import bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)


DEBUG = 1


def debug(*args, **kwargs):
    if DEBUG:
        print(*args, **kwargs)


t = iread()
for _ in range(t):
    n = iread()
    arr = viread()
    can = True
    for i in range(n - 1):
        if (arr[i] - arr[i + 1]) % 2 == 1:
            can = False
            break
    print(["NO", "YES"][int(can)])
