'''input
2
1 2
2
1 2
'''

import math
from collections import defaultdict as dd
import heapq

n = int(input())
a = [int(i) for i in input().split(" ")]
m = int(input())
b = [int(i) for i in input().split(" ")]

x = [a[0]]
y = [b[0]]
if sum(a) != sum(b):
    print(-1)
else:
    for i in range(1, n):
        x.append(x[-1] + a[i])
    for i in range(1, m):
        y.append(y[-1] + b[i])
    x = set(x)
    y = set(y)
    print(len(x.intersection(y)))
