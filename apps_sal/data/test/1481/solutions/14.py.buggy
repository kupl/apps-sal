import collections
import itertools


n = int(input())
m = collections.defaultdict(lambda: "x")
for y in range(n):

    for x, ch in enumerate(input()):

        m[x, y] = ch

deltas = ((-1, 0), (0, -1), (1, 0), (0, 1))
for p in itertools.product(list(range(n)), repeat=2):

    cps = [tuple(map(sum, list(zip(p, dp)))) for dp in deltas]
    if len(tuple([cp for cp in cps if m[cp] == "o"])) % 2:

        print("NO")
        return

print("YES")
