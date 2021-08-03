[x, y] = [int(i) for i in input().split()]

if x >= 0:
    if y >= 0:
        print(0, ' ', x + y, ' ', x + y, ' ', 0)
    else:
        print(0, ' ', y - x, ' ', x - y, ' ', 0)
else:
    if y >= 0:
        print(x - y, ' ', 0, ' ', 0, ' ', y - x)
    else:
        print(x + y, ' ', 0, ' ', 0, ' ', x + y)
