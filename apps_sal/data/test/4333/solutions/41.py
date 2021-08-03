a, b, c, d = map(int, input().split())
s = c - a
t = d - b
x_3 = c - t
y_3 = d + s
x_4 = x_3 - s
y_4 = y_3 - t
print(str(x_3) + ' ' + str(y_3) + ' ' + str(x_4) + ' ' + str(y_4))
