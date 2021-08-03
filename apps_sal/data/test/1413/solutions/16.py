import math
import random
import sys
from collections import defaultdict as dd
ans = 0
n = int(input())
l = [int(i) for i in input()]
for i in range(n):
    if l[i] % 2 == 0:
        ans += (i + 1)
print(ans)
