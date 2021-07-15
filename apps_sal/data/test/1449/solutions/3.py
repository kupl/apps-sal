import sys,math
from collections import Counter,deque,defaultdict
from bisect import bisect_left,bisect_right 
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

for _ in range(inp()):
    n,k = inpl()
    a = inpl()
    ln = len(set(a))
    if k == 1 and ln > 1:
        print(-1)
        continue
    if ln == 1:
        print(1)
        continue
    ln -= 1
    k -= 1
    print((ln+k-1)//k)
