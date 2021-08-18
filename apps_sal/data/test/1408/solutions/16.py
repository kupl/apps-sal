from bisect import bisect_left as bl, bisect_right as br, insort
import sys
import heapq
from collections import defaultdict as dd, deque
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))


mod = int(1e9 + 7)

n = int(data())
dp1 = []
dp2 = []
for i in range(n):
    t, w = mdata()
    if t == 1:
        dp1.append(w)
    else:
        dp2.append(w)
dp1.sort(reverse=True)
dp2.sort(reverse=True)
s = len(dp1) + 2 * len(dp2)
k = 0
flag = True
while flag:
    flag = False
    if len(dp2) > 0:
        if len(dp1) > 1:
            m = min(dp1[-1] + dp1[-2], dp2[-1])
            if k + m <= s - 2:
                if m == dp2[-1]:
                    dp2.pop()
                    k += m
                    s -= 2
                else:
                    k += dp1.pop()
                    s -= 1
                flag = True
        else:
            if len(dp2) > 0 and dp2[-1] + k <= s - 2:
                k += dp2.pop()
                s -= 2
                flag = True
    if flag == False:
        if len(dp1) > 0 and dp1[-1] + k <= s - 1:
            k += dp1.pop()
            s -= 1
            flag = True
print(s)
