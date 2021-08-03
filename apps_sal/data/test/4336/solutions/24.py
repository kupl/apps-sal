w, h, x, y = map(int, input().split())
s = h * w / 2
p = 0
if w / 2 == x and h / 2 == y:
    p = 1
print(s, p)
