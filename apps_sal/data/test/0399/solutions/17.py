(x, y) = map(int, input().split())
if y == 0:
    print('No')
elif y == 1:
    if x > 0:
        print('No')
    else:
        print('Yes')
elif x == 0:
    if y == 1:
        print('Yes')
    else:
        print('No')
elif y == x + 1:
    print('Yes')
elif x >= y - 1 and (x - (y - 1)) % 2 == 0:
    print('Yes')
else:
    print('No')
