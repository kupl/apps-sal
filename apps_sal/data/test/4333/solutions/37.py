(x1, y1, x2, y2) = map(int, input().split(' '))
x2 -= x1
y2 -= y1
x3 = x4 = -x1
y3 = y4 = -y1
x4 = -y2
y4 = x2
x3 = x2 + x4
y3 = y2 + y4
print(x3 + x1, y3 + y1, x4 + x1, y4 + y1)
