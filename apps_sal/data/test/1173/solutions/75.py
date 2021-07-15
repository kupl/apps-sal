from collections import Counter,defaultdict,deque
from bisect import bisect_left
import sys,math,itertools,pprint,fractions,time
sys.setrecursionlimit(10**8)
mod = 10**9+7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))

st = time.time()
n = inp()
a = []
for i in range(n):
    b = inpl()
    a.append(deque(b))
zan = n*(n-1)//2
res = 0
while True:
    res += 1
    now = zan
    s = set()
    for i in range(n):
        if i in s or a[i] == deque([]): continue
        end = True
        chk = a[i][0] - 1
        if not chk in s and a[chk][0] == i+1:
            zan -= 1
            if not zan: 
                print(res); return
            a[i].popleft(); a[chk].popleft()
            s.add(i); s.add(chk)
        # print(res,i,chk,a)
        nnn = time.time()
    if now == zan:
        print((-1))
        return
    if nnn - st > 1.7:
        print((n*(n-1)//2))
        return

            

