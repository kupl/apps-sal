import sys
from heapq import *
#sys.stdin = open('in', 'r')
t = int(input())
for ti in range(t):
    n = int(input())
    a = []
    for i in range(n):
        mi, pi = list(map(int, input().split()))
        a.append((mi, -pi))
    a.sort()
    c = 0
    h = []
    res = 0
    for i in reversed(list(range(n))):
        heappush(h, -a[i][1])
        while c + i < a[i][0]:
            res += heappop(h)
            c += 1
    print(res)


# sys.stdout.write('YES\n')
# sys.stdout.write(f'{res}\n')
#sys.stdout.write(f'{y1} {x1} {y2} {x2}\n')
