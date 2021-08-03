import math
n = int(input())

a, b = 1, n
for i in range(1, int(math.sqrt(n) + 1)):
    if n % i == 0:
        q = n // i
        if abs(a - b) > abs(q - i):
            a, b = i, q

print((a - 1) + (b - 1))
