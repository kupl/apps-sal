p, q = 0, 1
for x in map(int, input()):
    p, q = min(p + x, q + 10 - x), min(p + x + 1, q + 9 - x)
print(p)
