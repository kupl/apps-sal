(h, w) = list(map(int, input().split()))
a1 = min(h * (w % 3 != 0), w * (h % 3 != 0))
a2 = 10 ** 6
a3 = 10 ** 6
for i in range(1, h):
    mx = max(w * i, w // 2 * (h - i), (w + 1) // 2 * (h - i))
    mn = min(w * i, w // 2 * (h - i), (w + 1) // 2 * (h - i))
    a2 = min(a2, mx - mn)
for i in range(1, w):
    mx = max(h * i, h // 2 * (w - i), (h + 1) // 2 * (w - i))
    mn = min(h * i, h // 2 * (w - i), (h + 1) // 2 * (w - i))
    a3 = min(a3, mx - mn)
print(min(a1, a2, a3))
