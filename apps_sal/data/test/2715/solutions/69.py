K = int(input())
d, m = divmod(K, 50)

A = [d + 49 - m] * (50 - m) + [d + 100 - m] * m
print(50)
print(*A)
