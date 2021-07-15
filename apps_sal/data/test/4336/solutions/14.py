w, h, x, y = map(int, input().split())
area = w * h
if x == w / 2 and y == h / 2:
    print(str(area / 2), "1")
else:
    print(str(area / 2), "0")
