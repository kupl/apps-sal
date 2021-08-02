from math import floor, ceil, pi
from collections import Counter, defaultdict

BS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def to_base(s, b):
    res = ""
    while s:
        res += BS[s % b]
        s //= b
    return res[::-1] or "0"


alpha = "abcdefghijklmnopqrstuvwxyz"

t = int(input())
for i in range(t):
    s = list(input())
    ans = s[0]
    for i in range(1, len(s), 2):
        ans += s[i]
    print(ans)
