(a, b, c) = (int(s) for s in input().split())
x = (a + b - c) // 2
y = b - x
z = c - y
if 2 * x == a + b - c and x >= 0 and y >= 0 and z >= 0:
    print(x, y, z)
else:
    print('Impossible')
