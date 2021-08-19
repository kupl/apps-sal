a, b, x, y = list(map(int, input().split()))

# using staircase:
if b < a:
    d1 = abs(b + 1 - a) * y + x
    d2 = (abs(b - a) * 2 - 1) * x
else:
    d1 = abs(b - a) * y + x
    d2 = (abs(b - a) * 2 + 1) * x
# using corridors only
# a10->b9->a9->b8..
print((min(d1, d2)))
