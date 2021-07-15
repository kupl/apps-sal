import sys
read = lambda t=int: list(map(t,sys.stdin.readline().split()))
array = lambda *ds: [array(*ds[1:]) for _ in range(ds[0])] if ds else 0

from collections import Counter

xs = read()
s, = read(str)

cnt = Counter()
a = 0
res = 0
for c in s:
    res += cnt[(c,a)]
    a += xs[ord(c)-ord('a')]
    cnt[(c,a)] += 1

print(res)

