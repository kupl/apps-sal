(r, g, b) = map(int, input().split())
print(min(r + g, r + b, b + g, (r + b + g) // 3))
