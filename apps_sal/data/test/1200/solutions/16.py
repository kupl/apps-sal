import math
from functools import reduce

n = input()

ints = [int(x) for x in input().split(' ')]
ints = sorted(ints)
dists = [ints[x] - ints[x - 1] for x in range(1, len(ints))]

gcd = reduce(math.gcd, dists)

ans = reduce(lambda a, b: a + (b // gcd - 1), dists, 0)

print(ans)
