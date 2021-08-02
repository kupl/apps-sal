def cut(ch, cw):
    total = ch * cw
    if not ch % 2 or not cw % 2:
        x = ch * cw // 2
        return x, x
    else:
        x = max(ch * (cw // 2), cw * (ch // 2))
        return x, total - x


h, w = map(int, input().split())

ans = h * w

for i in range(2):
    yh = h // 3 + i
    s = [yh * w]
    ch = h - yh
    s += cut(ch, w)
    ans = min(ans, max(s) - min(s))

for i in range(2):
    yw = w // 3 + i
    s = [h * yw]
    cw = w - yw
    s += cut(h, cw)
    ans = min(ans, max(s) - min(s))

print(ans)
