a, b, c, d = list(map(int, input().split()))
a, b, c = sorted([a, b, c])
print(max(0, d - (b - a)) + max(0, d - (c - b)))

