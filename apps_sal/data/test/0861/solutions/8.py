m, r = map(int, input().split())
print(2 * r * (m + (2 + 2 ** 0.5) * (m - 1) + (m - 1) * (m - 2) * (m / 3 + 2 ** 0.5)) / (m * m))
