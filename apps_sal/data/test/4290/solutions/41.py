(N, M) = map(int, input().split())
all = (N + M) * (N + M - 1) // 2
odd = N * M
print(all - odd)
