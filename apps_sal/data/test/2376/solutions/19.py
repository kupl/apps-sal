import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd


def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, W = MAP()
wv = [LIST() for _ in range(N)]
w0 = wv[0][0]

dic = defaultdict(list)
for w, v in wv:
    dic[w].append(v)

for key in dic:
    dic[key].sort(reverse=True)
    dic[key] = [0] + dic[key]
    dic[key] = list(accumulate(dic[key]))

for x in [w0, w0 + 1, w0 + 2, w0 + 3]:
    if not dic[x]:
        dic[x] = [0]
# print(dic)

ans = 0
for a in range(len(dic[w0])):
    for b in range(len(dic[w0 + 1])):
        for c in range(len(dic[w0 + 2])):
            for d in range(len(dic[w0 + 3])):
                w = w0 * a + (w0 + 1) * b + (w0 + 2) * c + (w0 + 3) * d
                s = dic[w0][a] + dic[w0 + 1][b] + dic[w0 + 2][c] + dic[w0 + 3][d]
                if w <= W:
                    ans = s if ans < s else ans
print(ans)
