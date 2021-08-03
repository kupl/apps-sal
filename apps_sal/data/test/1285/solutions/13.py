from math import gcd
from functools import reduce
import sys
import os
# Testing burritos code
d = sys.stdin.read().splitlines()


class Tab(object):
    def __init__(self):
        self.value = [0 for _ in range(n + 1)]

    def set_one(self, ind):
        if ind == 1:
            print(1)
            return
        else:
            self.value[ind] = 1

    def ones(self):
        return [index for index in range(n + 1) if self.value[index] == 1]


n = int(d[0])
cur_tab = Tab()


def group(l):
    cur = 1
    for x in range(1, n):
        if l[x] == l[x - 1]:
            cur += 1
        else:
            cur_tab.set_one(cur)
            cur = 1
    cur_tab.set_one(cur)


mat = [None for _ in range(n)]
euh = 0

for line in d[1:]:
    s = str(bin(int(line, 16)))[2:].zfill(n)
    mat[euh] = s
    euh += 1
    group(s)
for i in range(n):
    cur = 1
    for x in range(1, n):
        if mat[x][i] == mat[x - 1][i]:
            cur += 1
        else:
            cur_tab.set_one(cur)
            cur = 1
    cur_tab.set_one(cur)
print(reduce(gcd, cur_tab.ones()))
