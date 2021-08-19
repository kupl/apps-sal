(n, m) = list(map(int, input().split()))
k = n // m
rest = [0] * m
for i in range(1, m + 1):
    rest[i ** 2 % m] += k
for i in range(1, n % m + 1):
    rest[i ** 2 % m] += 1
r = rest[0] ** 2
for i in range(1, m):
    r += rest[i] * rest[-i]
print(r)
