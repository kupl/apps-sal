n = int(input())

a = [0] * (n + 1)

ca = 1
for i in range(2, n + 1):
    if a[i] != 0:
        continue
    m = 1
    while i * m <= n:
        a[i * m] = ca
        m += 1
    ca += 1

print(*a[2:n + 1])
