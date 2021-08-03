w, h, x, y = map(int, input().split())
area = w * h / 2
m = 0
if x * 2 == w and y * 2 == h:
    m = 1

print(area, m)
