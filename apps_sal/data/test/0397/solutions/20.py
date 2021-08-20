import math
(n, k) = map(int, input().split())
q = int(-3 + math.sqrt(9 + 8 * (n + k))) // 2
r = n - q
print(r)
