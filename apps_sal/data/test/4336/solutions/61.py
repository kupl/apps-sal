(w, h, x, y) = map(int, input().split())
s = 0.5 * w * h
i = 0
if 2 * x == w and 2 * y == h:
    i += 1
print(s, i)
