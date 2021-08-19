(n, f) = (int(input()), 3)
while n % f == 0:
    f *= 3
print(n // f + 1)
