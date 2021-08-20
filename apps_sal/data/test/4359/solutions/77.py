A = [int(input()) for _ in range(5)]
print(sum((((x - 1) // 10 + 1) * 10 for x in A)) - max(((10 - x % 10) % 10 for x in A)))
