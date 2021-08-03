import math
from collections import Counter
import itertools


def ii(): return int(input())
def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


a, b, c = mi()
ans = (a * (a + 1) // 2) * (b * (b + 1) // 2) * (c * (c + 1) // 2)
print(ans % 998244353)
