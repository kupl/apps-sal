(x, y) = map(int, input().split())
if y % 2 == 0 and y >= 2 * x and (4 * x >= y):
    print('Yes')
else:
    print('No')
