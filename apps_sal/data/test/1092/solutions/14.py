import itertools
import math


def countEndgames(grid):
    ls = []
    for elt, gp in itertools.groupby(grid):
        if elt == '.':
            ls.append(len(list(gp)))
    tot = 1
    for i, g in enumerate(ls):
        if i == 0 and grid[0] == '.' or i == (len(ls) - 1) and grid[-1] == '.':
            continue
        tot *= 2**(g - 1)
    tot *= math.factorial(sum(ls))
    for g in ls:
        tot //= math.factorial(g)
    return tot % (10**9 + 7)


n, x = list(map(int, input().split()))
ls = list(map(int, input().split()))
grid = ['.' for i in range(n)]
for x in ls:
    grid[x - 1] = '#'
print(countEndgames(grid))
