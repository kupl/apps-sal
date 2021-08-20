import math as mt
(a, b) = map(int, input().split())
n = 1
while a + (a - 1) * (n - 1) < b:
    n += 1
print(n if b != 1 else 0)
