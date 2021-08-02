N = int(input())
print(sum(N // n * (N // n + 1) * n // 2 for n in range(1, 1 + N)))
