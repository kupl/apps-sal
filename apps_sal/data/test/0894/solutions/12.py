data = input().split(" ")
x = int(data[0])
y = int(data[1])

sign_x = -1
sign_y = -1

if x > 0:
    sign_x = 1
if y > 0:
    sign_y = 1

value = abs(x) + abs(y)

if sign_x == 1 and sign_y == 1:
    print("0 %s %s 0" % (value * sign_x, value * sign_y))
elif sign_x == 1 and sign_y == -1:
    print("0 %s %s 0" % (value * sign_y, value * sign_x))
elif sign_x == -1 and sign_y == -1:
    print("%s 0 0 %s" % (value * sign_x, value * sign_y))
elif sign_x == -1 and sign_y == 1:
    print("%s 0 0 %s" % (value * sign_x, value * sign_y))
