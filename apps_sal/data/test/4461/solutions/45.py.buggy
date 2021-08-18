h, w = map(int, input().split())
if h == 2 and w == 2:
    print(1)
    return
ans = 10**10
if h >= 3:
    if h % 3 == 0:
        a = 0
    else:
        a = w
    if a < ans:
        ans = a
if w >= 3:
    if w % 3 == 0:
        a = 0
    else:
        a = h
    if a < ans:
        ans = a
if h > 1:
    b = h // 3
    x1 = w * b
    x2 = (h - b) * (w // 2)
    x3 = h * w - x1 - x2
    a = max(x1, x2, x3) - min(x1, x2, x3)
    if a < ans:
        ans = a
    x1 = w * (b + 1)
    x2 = (h - b - 1) * (w // 2)
    x3 = h * w - x1 - x2
    a = max(x1, x2, x3) - min(x1, x2, x3)
    if a < ans:
        ans = a
    b = w // 3
    x1 = h * b
    x2 = (w - b) * (h // 2)
    x3 = h * w - x1 - x2
    a = max(x1, x2, x3) - min(x1, x2, x3)
    if a < ans:
        ans = a
    x1 = h * (b + 1)
    x2 = (w - b - 1) * (h // 2)
    x3 = h * w - x1 - x2
    a = max(x1, x2, x3) - min(x1, x2, x3)
    if a < ans:
        ans = a
print(ans)
