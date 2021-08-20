(H, W) = map(int, input().split())
h = min(H, W)
w = max(H, W)
s = h * w
res = 10 ** 10
for i in range(1, w):
    a = h * i
    b = (w - i) // 2 * h
    c = s - a - b
    res = min(max(a, b, c) - min(a, b, c), res)
    b = (w - i) * (h // 2)
    c = s - a - b
    res = min(max(a, b, c) - min(a, b, c), res)
for i in range(1, h):
    a = w * i
    b = (h - i) // 2 * w
    c = s - a - b
    res = min(max(a, b, c) - min(a, b, c), res)
    b = (h - i) * (w // 2)
    c = s - a - b
    res = min(max(a, b, c) - min(a, b, c), res)
print(res)
