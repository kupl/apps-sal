n = int(input())
w, h = 0, 0
width = True
while w * h < n:
    if width:
        w += 1
    else:
        h += 1
    width = not width
print(w + h)

