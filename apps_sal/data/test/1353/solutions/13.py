import math
n, m, a, b = list(map(int, input().split()))
a1 = math.ceil(n / m) * b
a2 = n * a
a3 = n // m * b + (n % m) * a
print(min([a1, a2, a3]))
