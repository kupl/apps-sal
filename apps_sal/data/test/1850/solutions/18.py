import sys
from sys import stdin, stdout
(n, d) = map(int, stdin.readline().split(' '))
ini = list(map(int, stdin.readline().split(' ')))
poi = list(map(int, stdin.readline().split(' ')))
maxp = ini[d - 1] + poi[0]
ctr3 = 0
for i in range(d - 1):
    if ini[i] + poi[-1] <= maxp:
        ctr3 += 1
        poi.pop(-1)
print(d - ctr3)
