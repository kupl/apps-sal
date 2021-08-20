n = int(input())
print(n // 2 + 1)
for c in range(1, n + 1):
    if c <= n // 2 + 1:
        print(c, 1)
    else:
        print(n // 2 + 1, c - n // 2)
