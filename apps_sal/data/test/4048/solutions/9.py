n = int(input())
m = 10**12
for i in range(1, 10**6 + 1):
    if n % i == 0:
        m = min(m, i + (n // i))

print(m - 2)
