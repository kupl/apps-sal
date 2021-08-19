from sys import stdin
from functools import lru_cache
from collections import defaultdict
infile = stdin
(N, K) = map(int, infile.readline().split())
watched = infile.readline().strip()
mem = set()
mem.add((0, 0, 0))
for (i, letter) in enumerate(watched):
    for d in range(K + 1):
        for c in range(K + 1):
            if (i, d, c) in mem:
                if letter in ('N', '?'):
                    mem.add((i + 1, max(d, c + 1), c + 1))
                if letter in ('Y', '?'):
                    mem.add((i + 1, d, 0))


def good():
    for (i, d, c) in mem:
        if i == N and d == K:
            return 'YES'
    return 'NO'


print(good())
