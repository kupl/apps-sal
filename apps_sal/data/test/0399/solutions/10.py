(x, y) = list(map(int, input().split()))
if x > 0 and y == 1 or y == 0:
    print('No')
else:
    (a, b) = (y - 1, y)
    if a > x:
        print('No')
    else:
        print(('No', 'Yes')[(x - a) % 2 == 0])
