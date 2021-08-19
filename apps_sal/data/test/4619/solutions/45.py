(w, h, n) = list(map(int, input().split()))
(i, j) = (0, 0)
for _ in range(n):
    (x, y, a) = list(map(int, input().split()))
    if a == 1:
        i = max(i, x)
    elif a == 2:
        w = min(w, x)
    elif a == 3:
        j = max(j, y)
    else:
        h = min(h, y)
print((w - i) * (h - j) if w > i and h > j else 0)
