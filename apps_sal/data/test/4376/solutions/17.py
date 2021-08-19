import bisect
import itertools
(n, m) = map(int, input().split())
aa = list(map(int, input().split()))
(a, c) = ([0] + list(itertools.accumulate(aa)), 0)
for b in input().split():
    b = int(b)
    f = bisect.bisect_left(a, b, lo=c)
    k = b - a[f - 1]
    print(f, k)
    c = max(c, f)
