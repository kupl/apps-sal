N = int(input())
V = sum([i * (N - i + 1) for i in range(1, N + 1)])
E = 0
for i in range(N - 1):
    a, b = list(map(int, input().split()))
    a, b = min(a, b), max(a, b)
    E += a * (N - b + 1)
print((V - E))
