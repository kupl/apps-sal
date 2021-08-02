from operator import sub
from bisect import bisect
n = int(input())
a = sorted(map(int, input().split()))
b = sorted(map(sub, a[1:], a))
d = b[0]
i = bisect(b, d)
print(d, i)
