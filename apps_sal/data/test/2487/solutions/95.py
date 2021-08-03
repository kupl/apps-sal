n = int(input())
V = n * (n + 1) * (n + 2) // 6
E = 0
for _ in range(n - 1):
    u, v = list(map(int, input().split()))
    if u > v:
        u, v = v, u
    E += u * (n - v + 1)
print((V - E))
