from sys import stdin, stdout
import math
import copy
s = input()
N = int(s, 2)
res = 0
T = 1
while T < N:
    res += 1
    T *= 4
print(res)
