(w, h, n) = map(int, input().split())
chk = [0] * 101
wx = [1] * w
wy = [1] * h
for _ in range(n):
    (x, y, a) = map(int, input().split())
    if a == 1:
        wx[:x] = chk[:x]
    elif a == 2:
        wx[x:] = chk[x + 1:w - 1]
    elif a == 3:
        wy[:y] = chk[:y]
    else:
        wy[y:] = chk[y + 1:h - 1]
ws = wx.count(1) * wy.count(1)
print(ws)
