a, b = [int(v) for v in input().split()]
x, y, z = [int(v) for v in input().split()]

ra = 2 * x + y
rb = y + 3 * z

print(max(ra - a, 0) + max(rb - b, 0))
