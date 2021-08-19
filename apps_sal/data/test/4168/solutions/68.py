from decimal import Decimal
from copy import deepcopy
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
from bisect import bisect_right
from bisect import bisect_left
from collections import deque
import math
import fractions
from collections import Counter
from collections import defaultdict
from itertools import combinations
from itertools import permutations
from itertools import accumulate
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)
alf = list('abcdefghijklmnopqrstuvwxyz')
ALF = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
INF = float('inf')
s = ''
N = int(input())
if N == 0:
    print(0)
else:
    while N != 0:
        x = N % -2
        if x == 0:
            s = '0' + s
            N = N // -2
        else:
            N = N // -2 + 1
            s = '1' + s
    print(s)
