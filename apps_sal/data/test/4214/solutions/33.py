from math import factorial
from itertools import permutations

n = int(input())
t, *c = [list(map(int, input().split())) for _ in range(n)]

print(sum(sum(((x - v)**2 + (y - w)**2)**.5 for (x, y), (v, w) in zip([t] + l, l + [t])) for l in map(list, permutations(c))) * (n - 1) / factorial(n))
