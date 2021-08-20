(r, g, b) = tuple(map(int, input().split()))
if r > 2 * (g + b):
    r = 2 * (g + b)
if b > 2 * (g + r):
    b = 2 * (g + r)
if g > 2 * (r + b):
    g = 2 * (r + b)
print(int((g + r + b) / 3))
