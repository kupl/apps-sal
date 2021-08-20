(h, w) = list(map(int, input().split()))
mi = h * w
s = h * w
for i in range(h):
    s1 = w * i
    if w % 2 == 0 or (h - i) % 2 == 0:
        s2 = (s - s1) // 2
        s3 = s2
    elif h - i < w:
        s2 = (h - i) * (w - 1) // 2
        s3 = (h - i) * (w + 1) // 2
    else:
        s2 = (h - i - 1) // 2 * w
        s3 = (h - i + 1) // 2 * w
    d = abs(min(s1, s2, s3) - max(s1, s2, s3))
    if d < mi:
        mi = d
for i in range(w):
    s1 = h * i
    if (w - i) % 2 == 0 or h % 2 == 0:
        s2 = (s - s1) // 2
        s3 = s2
    elif w - i < h:
        s2 = (w - i) * (h - 1) // 2
        s3 = (w - i) * (h + 1) // 2
    else:
        s2 = (w - i - 1) // 2 * h
        s3 = (w - i + 1) // 2 * h
    d = abs(min(s1, s2, s3) - max(s1, s2, s3))
    if d < mi:
        mi = d
print(mi)
