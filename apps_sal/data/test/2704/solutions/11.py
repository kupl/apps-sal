import collections
from collections import defaultdict
import math


n, z = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
p = min(a)
q = max(a)
for i in range(z):
    if p <= int(input()) <= q:
        print("Yes")
    else:
        print("No")
