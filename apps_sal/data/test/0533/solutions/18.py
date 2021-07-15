a1, a2, k1, k2, n = int(input()), int(input()), int(input()), int(input()), int(input())
if k1 > k2:
    k1, k2 = k2, k1
    a1, a2 = a2, a1
oleg = a1 * (k1 - 1) + a2 * (k2 - 1)
rm = max(0, n - oleg)
if n <= a1 * k1:
    rp = n // k1
else:
    rp = a1
    rp += (n - a1 * k1) // k2
print(rm, rp)
