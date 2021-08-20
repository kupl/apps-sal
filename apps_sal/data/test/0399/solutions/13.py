(x, y) = list(map(int, input().split()))
if y == 0:
    print('No')
elif y == 1 and x > 0:
    print('No')
elif y > x + 1:
    print('No')
elif (x - y) % 2 == 0:
    print('No')
else:
    print('Yes')
