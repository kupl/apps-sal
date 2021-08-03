#     Educational Codeforces Round 45 (Rated for Div. 2)
import collections
from functools import cmp_to_key
#key=cmp_to_key(lambda x,y: 1 if x not in y else -1 )

import sys


def getIntList():
    return list(map(int, input().split()))


n = getIntList()[0]

d1 = collections.defaultdict(lambda: 0)
d2 = collections.defaultdict(lambda: 0)

for i in range(n):
    s = input()
    m = len(s)
    acc1 = 0
    for j in range(m):
        if s[j] == '(':
            acc1 += 1
        else:
            acc1 -= 1
            if acc1 < 0:
                break
    acc2 = 0
    for j in range(m - 1, -1, -1):
        if s[j] == ')':
            acc2 += 1
        else:
            acc2 -= 1
            if acc2 < 0:
                break
    if acc2 >= 0:
        d2[acc2] += 1
    if acc1 >= 0:
        d1[acc1] += 1
# print(d1)
# print(d2)
res = 0
for x in d1:
    if x in d2:
        res += d1[x] * d2[x]
print(res)
