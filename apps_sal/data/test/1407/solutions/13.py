import heapq
from bisect import bisect_left, bisect_right
from collections import Counter
from itertools import accumulate

import math

R = lambda: list(map(int, input().split()))

def is_prime(num):
    return not any([num % i == 0 for i in range(2, int(math.sqrt(num) + 1))])

n, m = R()
grid = [list(R()) for i in range(n)]
primes = [x for x in range(2, 10**5 + 100) if is_prime(x)]
for i in range(n):
    for j in range(m):
        grid[i][j] = primes[bisect_left(primes, grid[i][j])] - grid[i][j]
min_row = min([sum(r) for r in grid])
min_col = min([sum(c) for c in zip(*grid)])
print(min(min_row, min_col))


