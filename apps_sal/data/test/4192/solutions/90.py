import sys
import heapq
import math
import fractions
import bisect
import itertools
from collections import Counter
from collections import deque
from operator import itemgetter
def input(): return sys.stdin.readline().strip()
def mp(): return map(int, input().split())
def lmp(): return list(map(int, input().split()))


d, t, s = mp()
if s * t - d >= 0:
    print("Yes")
else:
    print("No")
