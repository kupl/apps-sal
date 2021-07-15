from collections import Counter,defaultdict,deque
from heapq import heappop,heappush,heapify
import sys,bisect,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

a,b = inpl()
if a == b == 1:
    print(1,2)
    print('.#')
    return
rev = False
if a < b:
    rev = True
    a,b = b,a
a -= 1
res = [[None] * 100 for _ in range(100)]
r = 0
ok = True
while ok:
    for c in range(100):
        if r%2:
            res[r][c] = 0
        else:
            if not ok or c%2:
                res[r][c] = 1
                b -= 1
                if b == 0:
                    ok = False
            else:
                res[r][c] = 0
    r += 1
for c in range(100):
    res[r][c] = 1 if c == 99 else 0
r += 1
for c in range(100):
    res[r][c] = 1
r += 1
ok = True
while ok:
    for c in range(100):
        if r%2:
            res[r][c] = 1
        else:
            if not ok or c%2:
                res[r][c] = 0
                a -= 1
                if a <= 0:
                    ok = False
            else:
                res[r][c] = 1
    r += 1
for i in range(r,100):
    for j in range(100):
        res[i][j] = res[i-1][j]
print(100,100)
for i in range(100):
    for j in range(100):
        if rev:
            res[i][j] = '.' if res[i][j] else '#'
        else:
            res[i][j] = '#' if res[i][j] else '.'
    print(''.join(res[i]))
