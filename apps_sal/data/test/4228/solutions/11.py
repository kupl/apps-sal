N, L = map(int, input().split())

total = N * (L - 1) + N * (N + 1) / 2
lowest = 10 ** 10
for i in range(1, N + 1):
    y = L + i - 1
    lowest = min(lowest, abs(y))
print(int(total) - lowest) if total >= 0 else print(int(total) + lowest)
