#import sys
#import numpy as np
import math
#from fractions import Fraction
import itertools
from collections import deque
from collections import Counter
import heapq
from fractions import gcd
# input=sys.stdin.readline
#import bisect
from fractions import gcd

n = int(input())
p = set()
p.add(0)
ai = [int(input()) for _ in range(n)]
s = 0
cnt = 0
while True:
    a = ai[s]
    if a == 2:
        print(cnt + 1)
        return
    if a - 1 not in p:
        p.add(a - 1)
        cnt += 1
        s = a - 1
    else:
        print(-1)
        return
