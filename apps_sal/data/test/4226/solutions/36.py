X, Y = (int(x) for x in input().split())
a = 4 * X - Y
b = Y - 2 * X
if a >= 0 and b >= 0 and a % 2 == 0 and b % 2 == 0:
    print('Yes')
else:
    print('No')
