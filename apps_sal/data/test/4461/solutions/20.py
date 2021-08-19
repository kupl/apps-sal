(h, w) = map(int, input().split())
ans = 1000000000
if max(h, w) >= 3:
    if h >= w:
        ans = w * min(1, h % 3)
    else:
        ans = h * min(1, w % 3)
if h % 3 == 0:
    ans = 0
if w % 3 == 0:
    ans = 0
for i in range(1, h):
    ans_ = max(i * w, (h - i) * (w + w % 2) // 2) - min(i * w, (h - i) * (w - w % 2) // 2)
    ans = min(ans, ans_)
for i in range(1, w):
    ans_ = max(i * h, (w - i) * (h + h % 2) // 2) - min(i * h, (w - i) * (h - h % 2) // 2)
    ans = min(ans, ans_)
print(ans)
