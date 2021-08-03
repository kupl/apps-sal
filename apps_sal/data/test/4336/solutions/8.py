import sys
w, h, x, y = map(float, input().split())
S = w * h / 2
if x * 2 == w:
    if y * 2 == h:
        print(f'{S:.08f}' + " 1")

        return
print(f'{S:.08f}' + " 0")
