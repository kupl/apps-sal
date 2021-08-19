line = input()
(a, b) = line.split()
(a, b) = (int(a), int(b))
line = input()
(c, d) = line.split()
(c, d) = (int(c), int(d))
x = b
x_count = 1
y = d
y_count = 1
while y != x and y <= 10100 and (x <= 10100):
    if y > x:
        x = b + x_count * a
        x_count = x_count + 1
    else:
        y = d + y_count * c
        y_count = y_count + 1
if y == x:
    print(y)
else:
    print(-1)
