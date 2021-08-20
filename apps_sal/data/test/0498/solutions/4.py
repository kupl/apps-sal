import math
(n, m, k) = list(map(int, input().split()))
if k % 2 == 1:
    pos = 'L'
else:
    pos = 'R'
r = math.ceil(k / (2 * m))
k -= (r - 1) * 2 * m
f = math.ceil(k / 2)
print(r, f, pos)
