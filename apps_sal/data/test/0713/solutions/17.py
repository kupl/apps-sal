import math
import random

(n, m) = map(int, input().split())
n_points = n + 1 if n < m else m + 1
print(n_points)
for a in range(n_points)[::-1]:
    if n > m:
        print(n_points - 1 - a, a)
    else:
        print(a, n_points - 1 - a)
