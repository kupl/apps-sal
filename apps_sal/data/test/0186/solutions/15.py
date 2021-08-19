import collections
import math
(n, m) = list(map(int, input().split()))
x = min(2 * n, 3 * m) // 6
(a, b) = (2 * n, 3 * m)
while x:
    while a <= b and x:
        a += 2
        x -= 1
        if a % 6 == 0:
            a += 2
    while b < a and x:
        b += 3
        x -= 1
        if b % 6 == 0 and b < a:
            b += 3
        elif b % 6 == 0 and b == a:
            a += 2
print(max(a, b))
