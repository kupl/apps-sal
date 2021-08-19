(n, a, b, p, q) = list(map(int, input().split()))
a2 = a
b2 = b
while b2 != 0:
    (a2, b2) = (b2, a2 % b2)
print(n // a * p + n // b * q - n // (a * b // a2) * min(p, q))
