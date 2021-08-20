from collections import defaultdict
import math


def nCr(n, r):
    f = math.factorial
    if n == 1:
        return 0
    return f(n) // (f(r) * f(n - r))


n = int(input())
right_diag = defaultdict(int)
left_diag = defaultdict(int)
for _ in range(n):
    (x, y) = input().split()
    (x, y) = (int(x), int(y))
    right_diag[x - y] += 1
    left_diag[x + y] += 1
print(sum((nCr(val, 2) for val in right_diag.values())) + sum((nCr(val, 2) for val in left_diag.values())))
