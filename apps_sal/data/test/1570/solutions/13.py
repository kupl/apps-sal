k, n, w = map(int, input().split())
sw = w * (w + 1) / 2 * k
print(int(0) if n > sw else int(sw - n))
