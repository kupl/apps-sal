N = int(input())
sum_E = 0
for _ in range(N - 1):
    u, v = sorted(map(int, input().split()))
    sum_E += u * (N - v + 1)

sum_V = N * (N + 1) * (N + 2) // 6
print((sum_V - sum_E))
