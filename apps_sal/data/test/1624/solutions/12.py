import re
import math
import decimal
import bisect


def read():
    return input().strip()


def iread():
    return int(input().strip())


def viread():
    return [int(_) for _ in input().strip().split()]


n = iread()
arr = sorted(viread())
ans = 0
for i in range(n // 2):
    ans += (arr[i] + arr[-(i + 1)]) ** 2
print(ans)
