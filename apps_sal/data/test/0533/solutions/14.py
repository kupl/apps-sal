a1, a2, k1, k2, n = int(input()), int(input()), int(input()), int(input()), int(input())
max1 = 0
if k1 > k2:
    a1, a2, k1, k2 = a2, a1, k2, k1
if a1 * k1 >= n:
    max1 = n // k1
else:
    max1 = a1 + (n - a1 * k1) // k2
print(max(0, n - a1 * (k1 - 1) - a2 * (k2 - 1)), max1)
