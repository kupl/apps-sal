w, h, x, y = map(int, input().split())
print(w * h / 2, end=' ')
if x*2 == w and y*2 == h:
    print(1)
else:
    print(0)
