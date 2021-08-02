import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))


s = input()[::-1]
n = len(s)
a = [0] * 2019
a[0] = 1
c, d = 0, 1
for i in s:
    c += int(i) * d
    c %= 2019
    d *= 10
    d %= 2019
    a[c] += 1
ans = 0
for i in a:
    ans += i * (i - 1) // 2
print(ans)
