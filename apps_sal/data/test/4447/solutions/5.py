import sys
from collections import Counter


def i_ints():
    return list(map(int, sys.stdin.readline().split()))


(n, m) = i_ints()
a = list(i_ints())
r = [x % m for x in a]
c = Counter(r)
c = [c[i] for i in range(m)]
rem2ind = [[] for i in range(m)]
for (i, x) in enumerate(r):
    rem2ind[x].append(i)
R = n // m
for (i, inds) in enumerate(rem2ind):
    if len(inds) > R:
        next_big = i
        break
else:
    next_big = m
next_small = next_big + 1
moves = 0
while next_big < m:
    next_small = max(next_small, next_big + 1)
    num = max(c[next_big] - R, 0)
    while num > 0:
        num2 = max(R - c[next_small % m], 0)
        delta = min(num, num2)
        num -= delta
        c[next_small % m] += delta
        step = next_small - next_big
        for i in rem2ind[next_big][num:num + delta]:
            a[i] += step
        moves += delta * step
        if c[next_small % m] >= R:
            next_small += 1
    next_big += 1
print(moves)
print(' '.join(map(str, a)))
