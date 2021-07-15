w, h, x, y = map(int, input().split())

flg = 0
if x * 2 == w and y * 2 == h:
  flg = 1

print(w * h / 2, flg)
