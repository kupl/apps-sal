import bisect
import math
N = int(input())
a = list(map(int, input().split()))
a.sort()
n = a[-1]
harf = n / 2
ri = bisect.bisect_left(a, harf)
r = a[ri]
if ri > 0 and abs(harf - r) >= abs(harf - a[ri - 1]):
    r = a[ri - 1]
print(n, r)
