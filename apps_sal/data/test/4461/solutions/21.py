h, w = map(int, input().split())
INF = 100000000

# 縦に3つ分ける場合
if w % 3 == 0:
    s_tate = 0
else:
    s_tate = (int(w / 3) + 1) * h - int(w / 3) * h

# 横に3つに分ける場合
if h % 3 == 0:
    s_yoko = 0
else:
    s_yoko = (int(h / 3) + 1) * w - int(h / 3) * w

# 上側に縦に2つ、下方に1つでわける場合
case3 = INF
if w % 2 == 0:
    for i in range(1, h):
        buf = abs((int(w / 2) * i) - (w * (h - i)))
        case3 = min(buf, case3)
else:
    for i in range(1, h):
        buf1 = int(w / 2) * i
        buf2 = (int(w / 2) + 1) * i
        buf3 = w * (h - i)
        buf = [buf1, buf2, buf3]
        buf = sorted(buf)
        sa = buf[2] - buf[0]
        case3 = min(sa, case3)

# 左側に１つ、右側に横に２つでわける場合
case4 = INF
if h % 2 == 0:
    for i in range(1, w):
        buf = abs((int(h / 2) * i) - (h * (w - i)))
        case4 = min(buf, case4)
else:
    for i in range(1, w):
        buf1 = int(h / 2) * i
        buf2 = (int(h / 2) + 1) * i
        buf3 = h * (w - i)
        buf = [buf1, buf2, buf3]
        buf = sorted(buf)
        sa = buf[2] - buf[0]
        case4 = min(sa, case4)
ans1 = min(s_tate, s_yoko)
ans2 = min(case3, case4)

ans = min(ans1, ans2)

#print(s_tate, s_yoko, case3, case4)

print(ans)
