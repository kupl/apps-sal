h, w = map(int, input().split())
s = [h * w] * 4

if h == w == 2:
    print(1)
    return
if h % 3 == 0 or w % 3 == 0:
    print(0)
    return

if w > 2:
    s[0] = h
if h > 2:
    s[1] = w
if h % 2 == 0:
    s[2] = h // 2
else:
    tmp = h * w
    for i in range(w // 3, w // 3 + 2):
        s1 = i * h
        s2 = (w - i) * (h // 2)
        s3 = (w - i) * (h // 2 + 1)
        tmp = min(tmp, max(s1, s2, s3) - min(s1, s2, s3))
    s[2] = tmp
if w % 2 == 0:
    s[3] = w // 2
else:
    tmp = h * w
    for i in range(h // 3, h // 3 + 2):
        s1 = i * w
        s2 = (h - i) * (w // 2)
        s3 = (h - i) * (w // 2 + 1)
        tmp = min(tmp, max(s1, s2, s3) - min(s1, s2, s3))
    s[3] = tmp

print(min(s))
