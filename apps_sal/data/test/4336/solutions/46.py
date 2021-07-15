w, h, x, y = map(int, input().split())
s = w * h / 2
t = 0
if 2 * x == w and 2 * y == h:
    t = 1
print(s, t)
