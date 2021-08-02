w, h, x, y = map(int, input().split())
if x * 2 == w and y * 2 == h:
    c = 1
else:
    c = 0
print(w * h / 2, c)
