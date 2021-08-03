w, h, x, y = map(int, input().split())

s = 0

if w == x * 2 and h == y * 2:
    s += 1

print(h * w / 2, s)
