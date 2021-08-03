n = int(input())
print(sum(i * (n // i * (n // i + 1)) // 2 for i in range(1, n + 1)))
