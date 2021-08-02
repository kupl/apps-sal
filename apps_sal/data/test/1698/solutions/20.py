N, K = map(int, input().split())
F = list(reversed(sorted(map(int, input().split()))))
res = 0
for i in range((N + K - 1) // K):
    res += 2 * (F[i * K] - 1)
print(res)
