from heapq import *
l = list()
r = list()
q = int(input())
sb = 0
sr = 0
sl = 0
f = 0
for _ in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        f ^= 1
        _, a, b = t
        sb += b
        if f:
            c = heappushpop(r, a)
            sr += a - c
            heappush(l, -c)
            sl += c
        else:
            c = -heappushpop(l, -a)
            sl += a - c
            heappush(r, c)
            sr += c
    else:
        print(-l[0], l[0] * (len(r) - len(l)) + sr - sl + sb)
