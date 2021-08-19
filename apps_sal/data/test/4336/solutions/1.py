# 長方形のど真ん中の点を通る直線で分ければ半分にできます
w, h, x, y = list(map(float, input().split()))
half_w = w / 2
half_h = h / 2
max_area = w * h / 2
if x == half_w and y == half_h:
    print(("{:.9f} 1".format(max_area)))

else:
    print(("{:.9f} 0".format(max_area)))
