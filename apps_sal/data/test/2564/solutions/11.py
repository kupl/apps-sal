from math import floor, ceil, pi
import re
from collections import Counter, defaultdict

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(s, b):
    res = ""
    while s:
        res += BS[s % b]
        s //= b
    return res[::-1] or "0"


alpha = "abcdefghijklmnopqrstuvwxyz"


pattern = r"0+"

t = int(input())
for i in range(t):
    a, b, n = list(map(int, input().split()))
    c = 0
    while a <= n and b <= n:
        c += 1
        if a < b:
            a += b
        else:
            b += a
    print(c)
