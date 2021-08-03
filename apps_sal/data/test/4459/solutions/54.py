import math
from collections import Counter
from itertools import product


def ii(): return int(input())


def mi(): return map(int, input().split())
def li(): return list(map(int, input().split()))


n = ii()
a = li()

cnt = Counter(a)
ans = 0
for i, j in cnt.items():
    if i > j:
        ans += j
    else:
        ans += j - i
print(ans)
