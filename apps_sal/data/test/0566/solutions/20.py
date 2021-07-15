r, g, b = sorted(tuple(map(int, input().split())))
print(min(r + g, (r + g + b) // 3))
