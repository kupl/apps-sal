(x, y) = list(map(int, input().split()))
if y == 0:
    print('No')
elif y == 1:
    if x == 0:
        print('Yes')
    else:
        print('No')
else:
    x -= y - 1
    if x % 2 == 0 and x >= 0:
        print('Yes')
    else:
        print('No')
