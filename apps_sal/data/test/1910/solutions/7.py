n = int(input())
r1 = int((n - 3) * 4 * 9 * 4 ** (2 * n - 2 - n - 2))
r2 = int(2 * 4 * 3 * 4 ** (2 * n - 2 - n - 1))
print(r1 + r2)
