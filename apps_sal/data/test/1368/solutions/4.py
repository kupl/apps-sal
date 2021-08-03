from math import comb
from statistics import mean
N, A, B = map(int, input().split())
V = sorted([int(x) for x in input().split()], reverse=True)
maxmean = mean(V[:A])
if V[0] != V[A - 1]:
    n = V.count(V[A - 1])
    k = V[:A].count(V[A - 1])
    way = comb(n, k)
else:
    n = V.count(V[A - 1])
    way = sum(comb(n, k) for k in range(A, min(n, B) + 1))
print(maxmean)
print(way)
