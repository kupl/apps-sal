from itertools import permutations
from math import sqrt, factorial
n = int(input())
positions = [list(map(int, input().split())) for _ in range(n)]
perm = permutations(positions, n)
s = 0
for p in perm:
    for e in range(len(p)-1):
        xi, yi = p[e]
        xj, yj = p[e+1]
        s += sqrt((xj-xi)**2 + (yj-yi)**2)
print((s/factorial(n)))

