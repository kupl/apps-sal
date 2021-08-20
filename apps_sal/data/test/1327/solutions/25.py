from itertools import *
(N, M) = map(int, input().split())
C = [list(map(int, input().split())) for n in range(N)]
print(max([sum(sorted([i * x + j * y + k * z for (x, y, z) in C], reverse=True)[:M]) for (i, j, k) in product([-1, 1], [-1, 1], [-1, 1])]))
