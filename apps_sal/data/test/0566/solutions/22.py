(r, g, b) = list(map(int, input().split()))
z = min(r + g + b, 3 * min(r + b, min(g + b, g + r)))
print(z // 3)
