(x, y, x0, y0) = map(int, input().split())
print(x0, y0)
print(1, y0)
print(1, 1)
no = [(x0, y0), (1, y0), (1, 1)]
ltor = True
for a in range(1, x + 1):
    if ltor:
        for b in range(1, y + 1):
            if (a, b) not in no:
                print(a, b)
    else:
        for b in range(y, 0, -1):
            if (a, b) not in no:
                print(a, b)
    ltor = not ltor
