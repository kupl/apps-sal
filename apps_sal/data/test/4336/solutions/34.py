w, h, x, y = map(int, input().split())
che = 0
center = (w / 2, h / 2)
if (x, y) == center:
    che = 1
print(w * h / 2, che)
