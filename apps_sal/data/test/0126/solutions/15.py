from sys import setrecursionlimit, exit
from math import ceil, floor, acos, pi
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd
from functools import reduce
setrecursionlimit(10**8)
RI = lambda x=' ': list(map(int, input().rstrip().split(x)))
RS = lambda x=' ': input().rstrip().split(x)
dX = [-1, 1, 0, 0, -1, 1, -1, 1]
dY = [0, 0, -1, 1, 1, -1, -1, 1]
mod = int(1e9 + 7)
eps = 1e-6
MAX = 1010
n = RI()[0]
s = RS()[0]
pos = {}
acceptable = {}
for i in range(1, 10):
    pos[i] = ((i - 1) // 3 + 1, (i - 1) % 3 + 1)
pos[0] = (4, 2)
for v in list(pos.values()):
    acceptable[v] = 1
s = list(map(int, list(s)))
cnt = 0
for st in acceptable:
    curr = list(st)
    flag = 1
    for i in range(1, len(s)):
        curr[0] += pos[s[i]][0] - pos[s[i - 1]][0]
        curr[1] += pos[s[i]][1] - pos[s[i - 1]][1]
        if tuple(curr) not in acceptable:
            flag = 0
    if flag:
        cnt += 1
print("YES" if cnt == 1 else "NO")
