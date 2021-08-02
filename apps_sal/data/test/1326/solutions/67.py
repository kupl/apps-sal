N = int(input())
print(sum(N // i * (N // i + 1) * i // 2 for i in range(1, N + 1)))
