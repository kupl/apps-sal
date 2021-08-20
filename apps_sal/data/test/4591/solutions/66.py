(a, b, c, x, y) = map(int, input().split())
res = a * x + b * y
for i in range(1, max(x, y) + 1):
    ab = i * 2
    cand = ab * c + a * max(0, x - i) + b * max(0, y - i)
    res = min(res, cand)
print(res)
