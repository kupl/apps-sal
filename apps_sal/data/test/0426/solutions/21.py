import sys
import heapq
import math
from collections import defaultdict as dd

n, k = [int(i) for i in input().split()]
s = [i for i in input()]

if len(s) == 1 and k:
    print('0')
elif len(s) == 1 and k == 0:
    print(s[0])
else:

    if s[0] > '1' and k and len(s) > 1:
        s[0] = '1'
        k -= 1
    for i in range(1, n):
        if k:
            if s[i] > '0':
                s[i] = '0'
                k -= 1

        else:
            break
    print("".join(s))
