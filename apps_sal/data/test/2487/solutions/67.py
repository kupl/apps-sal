n = int(input())
V = n * (n + 1) * (n + 2) // 6
E = 0
for _ in range(n - 1):
    a, b = list(map(int, input().split()))
    if a > b:
        a, b = b, a
    E += a * (n - b + 1)
print((V - E))
