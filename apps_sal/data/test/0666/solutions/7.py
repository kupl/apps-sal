from math import sqrt
n = int(input())
k = (-1 + sqrt(1 + 8 * n)) // 2
if n - (k * k + k) // 2 != 0:
    k = n - (k * k + k) // 2
print(int(k))
