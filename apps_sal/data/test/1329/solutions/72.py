from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions,pprint
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

def conb(n,r): 
    if n<r: return 0
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
def prime_factorize(n):
    if n == 1:
        return [1]
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

n = inp()
d = defaultdict(int)
for i in range(1,n+1):
    for x in prime_factorize(i):
        d[x] += 1

valist = list(d.values())
c = [2,4,14,24,74]
cnt = [0] * 5
for x in valist:
    if x >= 74: cnt[4] += 1
    elif x >= 24: cnt[3] += 1
    elif x >= 14: cnt[2] += 1
    elif x >= 4: cnt[1] += 1
    elif x >= 2: cnt[0] += 1
# print(cnt)
res = 0
a = sum(cnt[1:]); b = cnt[0]
res += conb(a,3)*3 + conb(a,2)*b
a = sum(cnt[2:]); b = cnt[1]
res += a*(a-1) + a*b
a = sum(cnt[3:]); b = sum(cnt[:3])
res += a*(a-1) + a*b
res += cnt[4]
print(res)

