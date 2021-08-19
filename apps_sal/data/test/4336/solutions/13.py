(w, h, x, y) = map(int, input().split())
print(w * h / 2.0, 1 if x + x == w and y + y == h else 0)
