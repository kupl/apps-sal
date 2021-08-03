a, b, c, d = map(int, input().split())

overlap = max(0, (min(b, d) - max(a, c)))
print(overlap)
