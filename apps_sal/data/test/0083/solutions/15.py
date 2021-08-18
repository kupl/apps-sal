
import math
import os
import random
import re
import sys

n = int(input())
l = list(map(int, input().split()))
a, b = 0, 0
for i in l:
    if i > 0:
        a += 1
    elif i < 0:
        b += 1
t = (n + 1) // 2
if a >= t:
    print(1)
elif b >= t:
    print(-1)
else:
    print(0)
