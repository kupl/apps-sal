from collections import Counter,defaultdict,deque
from heapq import heappop,heappush
from bisect import bisect_left,bisect_right 
import sys,math,itertools,fractions
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

s = input()
n = len(s)
res = [0] * n
cnt = 0
now = [0,0]
for i in range(n):
    if s[i] == 'R':
        now[cnt%2] += 1
        cnt += 1
    else:
        res[i-1] += now[0]
        res[i] += now[1]
        now = [0,0]
        cnt = 0
for i in range(n)[::-1]:
    if s[i] == 'L':
        now[cnt%2] += 1
        cnt += 1
    else:
        res[i+1] += now[0]
        res[i] += now[1]
        now = [0,0]
        cnt = 0
print(*res)
