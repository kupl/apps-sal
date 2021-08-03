import math
import collections
from itertools import product


def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


s = list(input())
n = len(s)
ans = 0
for p in product((0, 1), repeat=n):
    total = 0
    for i in range(n):
        if p[i] == 1:
            ans += total
            total = 0
        else:
            total = total * 10 + int(s[i])
    ans += total
print(ans)
