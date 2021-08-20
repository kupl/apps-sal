import math
n = int(input())
(t, a) = (1, 1)
for _ in range(n):
    (T, A) = map(int, input().split())
    k = (T + t - 1) // T
    m = (A + a - 1) // A
    x = max(k, m)
    (t, a) = (x * T, x * A)
print(t + a)
