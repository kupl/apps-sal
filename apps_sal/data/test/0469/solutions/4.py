from math import sqrt
3
(r, h) = tuple(map(int, input().split()))
ans = (2 * h + r) // (2 * r)
print(2 * ans + (ans * r + sqrt(3.0) * r / 2 <= h + r))
