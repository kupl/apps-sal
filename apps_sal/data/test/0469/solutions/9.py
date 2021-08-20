(r, h) = map(int, input().split())
(d, p) = (3 ** 0.5 / 2 - 1, h / r)
print(max(1 + 2 * int(p - d), 2 * int(p + 0.5)))
