x1, y1, x2, y2 = list(map(int, input().split()))

if x1 == x2:
    d = abs(y2 - y1)
    print(x1 + d, y1, x2 + d, y2)
elif y1 == y2:
    d = abs(x1 - x2)
    print(x1, y1 + d, x2, y2 + d)
elif abs(x1 - x2) != abs(y1 - y2):
    print('-1')
else:
    d = abs(x1 - x2)
    if (min(x1, x2), max(y1, y2)) == (x1, y1) or\
            (min(x1, x2), max(y1, y2)) == (x2, y2):
        print(min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2))
    else:
        print(min(x1, x2), max(y1, y2), max(x1, x2), min(y1, y2))


