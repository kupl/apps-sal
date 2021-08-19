n = int(input())
print(n // 2 + 1)
for i in range(n):
    print(1 + n // 2 * (i // (n // 2 + 1)), i % (n // 2 + 1) + 1 + i // (n // 2 + 1))
