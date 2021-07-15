from math import *
from random import *
from bisect import *
from math import *
n = int(input())
mas = sorted(list(map(int, input().split())))
otv = [0 for i in range(n)]
nxt = 0
for i in range(1, n, 2):
    otv[i] = mas[nxt]
    nxt += 1
for i in range(0, n, 2):
    otv[i] = mas[nxt]
    nxt += 1
res = 0
for i in range(1, n - 1):
    if otv[i] < otv[i + 1] and otv[i] < otv[i - 1]:
        res += 1
print(res)
print(' '.join(map(str, otv)))
