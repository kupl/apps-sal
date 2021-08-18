from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
from math import *
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return map(int, data().split())


for i in range(int(data())):
    n = int(data())
    A = set(mdata())
    print(len(A))
