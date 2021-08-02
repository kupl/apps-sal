x, y = input().split()

x = int(x)
y = int(y)

if x > 0 and y > 0:
    x1 = 0
    y1 = x + y
    x2 = x + y
    y2 = 0

elif x < 0 and y > 0:
    x1 = x - y
    y1 = 0
    x2 = 0
    y2 = -x + y

elif x > 0 and y < 0:
    x1 = 0
    y1 = -x + y
    x2 = x + (-y)
    y2 = 0

else:
    x1 = x + y
    y1 = 0
    x2 = 0
    y2 = x + y


print(x1, ' ', y1, ' ', x2, ' ', y2)
