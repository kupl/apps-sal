__author__ = 'sandeepmellacheruvu'
from bisect import bisect_right
(n, m) = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
c = []
for (i, ele) in enumerate(b):
    p = bisect_right(a, ele)
    c.append(p)
for (i, ele) in enumerate(c):
    print(ele, end=' ')
print()
