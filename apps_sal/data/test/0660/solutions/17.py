import collections
import math

n, b, p = map(int, input().split())
ans, k, t = 0, 2, n
while k <= n:
    k *= 2
k //= 2
while n != 1:
    ans += (2 * b + 1) * (k // 2)
    n -= k // 2
    while k > n:
        k //= 2
print(ans, t * p)
