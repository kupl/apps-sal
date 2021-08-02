w, h, x, y = map(int, input().split())
if (x, y) == (w / 2, h / 2):
    print(w * h / 2, 1)
else:
    print(w * h / 2, 0)
