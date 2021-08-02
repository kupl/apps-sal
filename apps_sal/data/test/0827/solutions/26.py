import sys
input = sys.stdin.readline
# print=sys.stdout.write
# sys.setrecursionlimit(100000)
#from heapq import *
#from collections import deque as dq
#from math import ceil,floor,sqrt,gcd,log
#import bisect as bs
#from collections import Counter
#from collections import defaultdict as dc
#from functools import reduce
#from functools import lru_cache
ri = lambda: int(input())
rl = lambda: list(map(int, input().split()))
rs = lambda: input().strip("\r\n")
for _ in range(1):
    n = ri()
    t = rs()
    copies = 1e10
    ans = 0
    s = '110' * (n)
    for i in range(3):
        if t != s[i:i + n]: continue
        ans += copies - (i + n - 1) // 3
    print(int(ans))
