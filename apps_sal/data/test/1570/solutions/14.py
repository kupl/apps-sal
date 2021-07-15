k, n, w = map(int, input().split())
print(int(max(k * (((2 * 1 + w - 1) * w) / 2) - n, 0)))
