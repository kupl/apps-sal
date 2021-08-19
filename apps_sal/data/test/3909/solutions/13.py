(n, k) = (int(input()), 3)
while n % k == 0:
    k *= 3
print(n // k + 1)
