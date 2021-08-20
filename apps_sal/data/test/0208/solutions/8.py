(x1, y1, x2, y2) = map(int, input().split())
if x1 == x2:
    temp = abs(y1 - y2)
    x3 = x1 + temp
    x4 = x3
    print(x3, end=' ')
    print(y1, end=' ')
    print(x4, end=' ')
    print(y2, end=' ')
elif y1 == y2:
    temp = abs(x1 - x2)
    y3 = y1 + temp
    y4 = y3
    print(x1, end=' ')
    print(y3, end=' ')
    print(x2, end=' ')
    print(y4, end=' ')
elif abs(x1 - x2) == abs(y1 - y2):
    temp = abs(x1 - x2)
    x3 = x2
    x4 = x1
    y3 = y1
    y4 = y2
    print(x3, end=' ')
    print(y3, end=' ')
    print(x4, end=' ')
    print(y4, end=' ')
else:
    print('-1')
