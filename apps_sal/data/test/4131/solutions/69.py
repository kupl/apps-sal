from collections import defaultdict
from bisect import bisect

N, M = list(map(int, input().split()))
p = [tuple(map(int, input().split())) for _ in range(M)]
a = defaultdict(list)
for x, y in sorted(p):
    a[x] += [y]

for x, y in p:
    z = bisect(a[x], y)
    print(("%06d%06d" % (x, z)))
