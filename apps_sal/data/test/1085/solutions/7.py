from decimal import Decimal
from copy import deepcopy
import heapq
from heapq import heappush
from heapq import heappop
from heapq import heapify
import itertools
from bisect import insort_left
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
N = int(input())


def make_divisors(n):
    (lower_divisors, upper_divisors) = ([], [])
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


ans = {N}
li1 = make_divisors(N - 1)[1:]
for er in li1:
    ans.add(er)
li0 = make_divisors(N)[1:-1]
for i in li0:
    n = N
    while n % i == 0:
        n /= i
    if (n - 1) % i == 0:
        ans.add(i)
print(len(ans))
