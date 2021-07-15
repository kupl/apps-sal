c, v1, v2 = 0, 0, 0
for ch in input():
    c += 1 if ch == '+' else -1
    v1, v2 = min(v1, c), max(v2, c)
print(v2 - v1)

