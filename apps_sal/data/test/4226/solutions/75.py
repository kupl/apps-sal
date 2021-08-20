(x, y) = map(int, input().split())
a = 2 * x - y / 2
b = -x + y / 2
if int(a) + int(b) == x and a >= 0 and (b >= 0):
    print('Yes')
else:
    print('No')
