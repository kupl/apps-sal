from heapq import heappush, heappop, heappushpop
from itertools import permutations
from operator import itemgetter
from collections import deque
from collections import Counter
from itertools import accumulate
from collections import defaultdict
import sys
import math
from bisect import bisect_right as br
from bisect import bisect_left as bl
sys.setrecursionlimit(2147483647)
mod = 10 ** 9 + 7
inf = float('inf')


def I():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


t = I()
for _ in range(t):
    n = I()
    a = LI()
    if n % 2 == 0:
        x = Counter(a)
        for i in list(x.values()):
            if i % 2:
                print('First')
                break
        else:
            print('Second')
    else:
        print('Second')
