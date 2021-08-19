from bisect import *
from sys import *
p = list(map(int, stdin.read().split()))
t = [(p[i + 1], p[i], p[i + 2]) for i in range(1, len(p), 3)]
t.sort(reverse=True)
s = [(0, 0), (1000000000.0, 1e+16)]
for (b, a, h) in t:
    i = bisect(s, (b,))
    h += s[i - 1][1]
    j = bisect(s, (a,))
    while s[j][1] <= h:
        s.pop(j)
    s.insert(j, (a, h))
print(s[-2][1])
