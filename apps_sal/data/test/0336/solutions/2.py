n, a, b, c, d = [int(x) for x in input().split()]
possib = 0
for x in range(1, n + 1):
    if 1 <= (a + b + x - c - d) <= n and 1 <= (b + x - c) <= n and 1 <= (a + x - d) <= n:
        possib += 1
print(possib * n)
