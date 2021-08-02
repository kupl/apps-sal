from math import *
import os
import sys
from io import BytesIO

#input = BytesIO(os.read(0, os.fstat(0).st_size)).readline
n, k = list(map(int, input().split()))
s = input()
a = set(input().split())
n += 1
can1 = [0] * n
can2 = [0] * n
n -= 1
ans = 0
for i in range(n):
    if s[i] in a:
        can1[i + 1] = can1[i] + 1
    ans += can1[i + 1]
print(ans)
