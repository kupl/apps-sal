from itertools import *
(_, L) = open(0)
print(sum((sum(t) > 2 * max(t) for t in combinations(map(int, L.split()), 3) if len(set(t)) == 3)))
