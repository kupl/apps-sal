from collections import Counter
import sys


def read(t=int):
    return list(map(t, sys.stdin.readline().split()))


array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0
xs = read()
(s,) = read(str)
cnt = Counter()
a = 0
res = 0
for c in s:
    res += cnt[c, a]
    a += xs[ord(c) - ord('a')]
    cnt[c, a] += 1
print(res)
