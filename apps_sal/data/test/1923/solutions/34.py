import sys
import math
import random
import itertools
import bisect
from copy import copy
from collections import deque,Counter,defaultdict
from decimal import Decimal
def lcm(a,b): return a*b//math.gcd(a,b)
sys.setrecursionlimit(10 ** 9)
INF = 10**9

N = int(input())
L = list(map(int,input().split()))
L.sort()
ans = 0
for i in range(N):
    ans += L[i*2]
print(ans)
