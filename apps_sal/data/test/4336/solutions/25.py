w, h, x, y = map(int, input().split())
a = (w * h) / 2
if w % 2 == 0 and x == w // 2 and h % 2 == 0 and y == h // 2:
    print(a, 1)
else:
    print(a, 0)
