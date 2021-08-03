from sys import *
from math import *
from collections import *


M = {}

n = int(input())

for i in range(n):
    s = input()
    if s[0] not in M:
        M[s[0]] = 1
    else:
        M[s[0]] += 1

ans = 0

for m in M:
    if M[m] > 2:
        l = M[m] // 2
        r = M[m] - l
        if l >= 2:
            ans += l * (l - 1) // 2
        if r >= 2:
            ans += r * (r - 1) // 2
print(ans)
