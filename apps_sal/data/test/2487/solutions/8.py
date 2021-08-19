N = int(input())
M = 0
for _ in range(N - 1):
    (u, v) = sorted(map(int, input().split()))
    M += u * (N - v + 1)
V = 0
for r in range(1, N + 1):
    V += r * (N - r + 1)
print(V - M)
