h, w = list(map(int, input().split()))

ans = 10 ** 10
for i in range(h):
    x = (i + 1) * w
    mid = (h - i - 1) // 2
    y = mid * w
    z = (h - i - 1 - mid) * w
    ans = min(ans, max(x, y, z) - min(x, y, z))

    mid = w // 2
    y = (h - i - 1) * mid
    z = (h - i - 1) * (w - mid)
    ans = min(ans, max(x, y, z) - min(x, y, z))

for j in range(w):
    x = (j + 1) * h
    mid = (w - j - 1) // 2
    y = mid * h
    z = (w - j - 1 - mid) * h
    ans = min(ans, max(x, y, z) - min(x, y, z))

    mid = h // 2
    y = (w - j - 1) * mid
    z = (w - j - 1) * (h - mid)
    ans = min(ans, max(x, y, z) - min(x, y, z))

print(ans)

