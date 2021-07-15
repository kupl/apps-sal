n, m, mod = [int(x) for x in input().split()]

from functools import lru_cache
import sys
sys.setrecursionlimit(100000000)

@lru_cache(maxsize=None)
def rec(twos, ones):
    nonlocal mod
    if twos == 0 and ones == 0:
        return 1
    if twos == 1 and ones == 0:
        return 0
    else:
        count = 0
        # we can pick two from ones if there are at least two:
        if (ones >= 2):
            a = ones*(ones-1)//2
            b = rec(twos, ones-2)
            count += (a*b) % mod
        if (ones >= 1 and twos >= 1):
            a = ones*twos
            b = rec(twos-1, ones)
            count += (a*b) % mod
        if (twos >= 2):
            a = twos*(twos-1)//2
            b = rec(twos-2, ones+2)
            count += (a*b) % mod
        return count % mod

# we read the beginning matrix and calculate the starting position
matrix = []
for i in range(0, m):
    matrix.append([int(x) for x in input()])

twocount = 0
onecount = 0
for c in range(0, n):
    # for each column count the number of ones in it
    count = 0
    for r in range(0, m):
        # r is the row, c is the column
        if (matrix[r][c] == 1):
            count += 1
    if count == 2:
        twocount += 1
    elif count == 1:
        onecount += 1

ones = onecount
twos = n - onecount - twocount

print(rec(twos, ones))

