import sys
from heapq import *
#sys.stdin = open('in', 'r')
#n = int(input())
n, k = list(map(int, input().split()))
seg = []
for i in range(n):
    l, r = list(map(int, input().split()))
    seg.append((l, r, i + 1))
seg.sort()
c = 0
res = []
i = 0
hmin = []
hmax = []
rem = set()
while i < n:
    l, r, si = seg[i]
    while i < n and seg[i][0] == l:
        _, r, si = seg[i]
        heappush(hmax, (-r, si))
        heappush(hmin, (r, si))
        i += 1
        c += 1
    while len(hmin) > 0 and hmin[0][0] < l:
        mr, ind = heappop(hmin)
        if ind not in rem:
            c -= 1
    while c > k:
        mr, ind = heappop(hmax)
        res.append(ind)
        rem.add(ind)
        c -= 1
print(len(res))
if len(res) > 0:
    print(' '.join(map(str, res)))


# sys.stdout.write('YES\n')
# sys.stdout.write(f'{res}\n')
#sys.stdout.write(f'{y1} {x1} {y2} {x2}\n')
