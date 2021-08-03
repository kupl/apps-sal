h, w = map(int, input().split())
ans = min(h, w)
if h % 3 == 0 or w % 3 == 0:
    print(0)
    return
for hi in range(1, h):
    mi = min(w * hi, w // 2 * (h - hi), (w - w // 2) * (h - hi))
    ma = max(w * hi, w // 2 * (h - hi), (w - w // 2) * (h - hi))
    ans = min(ans, ma - mi)
for wi in range(1, w):
    mi = min(h * wi, h // 2 * (w - wi), (h - h // 2) * (w - wi))
    ma = max(h * wi, h // 2 * (w - wi), (h - h // 2) * (w - wi))
    ans = min(ans, ma - mi)
print(ans)
