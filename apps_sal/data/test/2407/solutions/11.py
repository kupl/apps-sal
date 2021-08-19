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
sys.setrecursionlimit(1000000)
mod = 10 ** 9 + 7
inf = float('inf')


def I():
    return int(sys.stdin.readline())


def LI():
    return list(map(int, sys.stdin.readline().split()))


q = I()
for _ in range(q):
    (n, r) = LI()
    x = LI()
    c = list(Counter(x).items())
    c.sort(key=itemgetter(0), reverse=True)
    ans = 0
    for (i, j) in c:
        if i - ans * r > 0:
            ans += 1
    print(ans)
