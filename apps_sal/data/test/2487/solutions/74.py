(N, *l) = map(int, open(0).read().split())
print(N * (N + 1) * (N + 2) // 6 - sum(((N - max(l[i], l[i + 1]) + 1) * min(l[i], l[i + 1]) for i in range(0, 2 * N - 2, 2))))
