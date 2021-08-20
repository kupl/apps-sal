(h, w) = map(int, input().split())
ans = h * w
for i in range(1, h):
    A = w * i
    if w % 2 == 0 or (h - i) % 2 == 0:
        B = (h - i) * w // 2
        C = (h - i) * w // 2
    elif h - i <= w:
        B = (h - i) * (w // 2 + 1)
        C = (h - i) * (w // 2)
    else:
        B = ((h - i) // 2 + 1) * w
        C = (h - i) // 2 * w
    ans = min(ans, max(A, max(B, C)) - min(A, min(B, C)))
for i in range(1, w):
    A = h * i
    if (w - i) % 2 == 0 or h % 2 == 0:
        B = (w - i) * h // 2
        C = (w - i) * h // 2
    elif w - i <= h:
        B = (w - i) * (h // 2 + 1)
        C = (w - i) * (h // 2)
    else:
        B = ((w - i) // 2 + 1) * h
        C = (w - i) // 2 * h
    ans = min(ans, max(A, max(B, C)) - min(A, min(B, C)))
print(ans)
