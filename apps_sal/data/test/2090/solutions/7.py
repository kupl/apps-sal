#!/usr/bin/env python3
import sys
import heapq


def rint():
    return list(map(int, sys.stdin.readline().split()))
#lines = stdin.readlines()


n, k = rint()

t = []
b = []
ind = []
for i in range(n):
    tt, bb = rint()
    t.append(tt)
    b.append(bb)
    ind.append(i)

ind.sort(key=lambda i: (-b[i], -t[i]))
# print(ind)

candi = 0
s = 0
cnt = 0
minb = 0
ans = 0
h = []
for i in range(n):
    bb = b[ind[i]]
    tt = t[ind[i]]
    if bb != minb:
        minb = bb
    heapq.heappush(h, (t[ind[i]], i))
    s += tt
    cnt += 1
    if cnt > k:
        tc, ic = heapq.heappop(h)
        s -= tc
        cnt -= 1
    candi = s * minb
    ans = max(candi, ans)

# for i in range(n):
#    print(heapq.heappop(h))
print(ans)
