import heapq
import sys
from collections import defaultdict, Counter
from itertools import product


n = int(input())

arr = list(map(int, input().split()))
c = Counter(arr)

if c[1] == 0:
    print('2 ' * n)
elif c[2] == 0:
    print('1 ' * n)
else:
    print('2 1 ' + '2 ' * (c[2] - 1) + '1 ' * (c[1] - 1))

