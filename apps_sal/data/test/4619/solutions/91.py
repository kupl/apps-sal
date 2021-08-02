w, h, n = list(map(int, input().split()))  # 初期値
lx = 0
ly = 0
rx = w
ry = h

for i in range(n):
    x, y, a = list(map(int, input().split()))

    if a == 1:
        if lx < x:
            lx = x
    elif a == 2:
        if rx > x:
            rx = x

    elif a == 3:
        if ly < y:
            ly = y

    else:
        if ry > y:
            ry = y
# 出力
print((max(rx - lx, 0) * max(ry - ly, 0)))
