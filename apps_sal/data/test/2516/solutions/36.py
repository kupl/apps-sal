from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions,copy
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

n,p = inpl()
t = list(input())[::-1]
res = 0
if p == 2 or p == 5:
    t = t[::-1]
    for i,x in enumerate(t):
        if int(x) % p == 0:
            res += i+1
    print(res)
    return
d = defaultdict(int)
now = 0
d[0] += 1
# print(t)
for i,x in enumerate(t):
    tmp = (pow(10,i,p) * int(x)) % p
    now += tmp
    now %= p
    d[now] += 1
# print(d)
for va in d.values():
    res += va*(va-1)//2
print(res)
