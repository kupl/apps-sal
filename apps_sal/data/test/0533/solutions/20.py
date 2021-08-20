a1 = int(input())
a2 = int(input())
k1 = int(input())
k2 = int(input())
n = int(input())
if k1 < k2:
    if a1 * k1 <= n:
        maximum = a1 + (n - a1 * k1) // k2
    else:
        maximum = n // k1
elif a2 * k2 <= n:
    maximum = a2 + (n - a2 * k2) // k1
else:
    maximum = n // k2
n -= a1 * (k1 - 1) + a2 * (k2 - 1)
if n <= 0:
    minimum = 0
else:
    minimum = n
print(minimum, maximum)
