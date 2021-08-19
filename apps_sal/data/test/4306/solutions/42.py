(a, b, c, d) = map(int, input().split())
r = min(b, d) - max(a, c)
print([0, r][r > 0])
