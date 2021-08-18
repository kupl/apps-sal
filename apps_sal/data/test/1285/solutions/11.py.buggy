from math import gcd
from functools import reduce
import sys
import os
d = sys.stdin.readlines()


n = int(d[0])
cur_tab = [0 for _ in range(n + 1)]


def group(l):
    cur = 1
    for x in range(1, n):
        if l[x] == l[x - 1]:
            cur += 1
        else:
            cur_tab[cur] = 1
            cur = 1
    cur_tab[cur] = 1
    if cur_tab[1] == 1:
        print(1)
        return


mat = [None for _ in range(n)]
euh = 0

for x in d[1:]:
    line = x[:-1]
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
            cur_tab[cur] = 1
            cur = 1
    cur_tab[cur] = 1
    if cur_tab[1] == 1:
        print(1)
        return
print(reduce(gcd, [index for index in range(n + 1) if cur_tab[index] == 1]))
