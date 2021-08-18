h, w = map(int, input().split())
if (h % 3 == 0 or w % 3 == 0):
    print(0)
    return
ans = float("inf")
if (w % 2 == 0):
    ans = min(ans, (h - h // 3) * (w // 2) - h // 3 * w)
    ans = min(ans, abs((h - h // 3 - 1) * (w // 2) - (h // 3 + 1) * w))
else:
    if (h % 3 == 1):
        ans = min(ans, max(abs((h - h // 3) * (w // 2) - h // 3 * w), abs((h - h // 3) * (w // 2 + 1) - h // 3 * w), abs(h - h // 3)))
    else:
        ans = min(ans, max(abs((h - h // 3 - 1) * (w // 2) - (h // 3 + 1) * w), abs((h - h // 3 - 1) * (w // 2 + 1) - (h // 3 + 1) * w), abs(h - h // 3 - 1)))
ans = min(ans, w)

a = w
w = h
h = a
# print(h,w)
if (w % 2 == 0):
    ans = min(ans, (h - h // 3) * (w // 2) - h // 3 * w)
    ans = min(ans, abs((h - h // 3 - 1) * (w // 2) - (h // 3 + 1) * w))
else:
    if (h % 3 == 1):
        ans = min(ans, max(abs((h - h // 3) * (w // 2) - h // 3 * w), abs((h - h // 3) * (w // 2 + 1) - h // 3 * w), abs(h - h // 3)))
    else:
        ans = min(ans, max(abs((h - h // 3 - 1) * (w // 2) - (h // 3 + 1) * w), abs((h - h // 3 - 1) * (w // 2 + 1) - (h // 3 + 1) * w), abs(h - h // 3 - 1)))
ans = min(ans, w)

print(ans)
