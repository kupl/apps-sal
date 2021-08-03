import math

k = int(input())
x, y = list(map(int, input().split()))

if k % 2 == 0 and (x + y) % 2 == 1:
    print((-1))
    return

a = 1
b = 1
d = 0
if x < 0:
    x *= -1
    a = -1
if y < 0:
    y *= -1
    b = -1
if x < y:
    d = 1
    x, y = y, x


def show_xy(tx, ty):
    if d == 1:
        print((ty * a, tx * b))
    else:
        print((tx * a, ty * b))


if x + y < k and (x + y) % 2 == 1:
    print((3))
    temp_x = x
    temp_y = x - k
    show_xy(temp_x, temp_y)
    temp_x = x + (k + x - y) // 2
    temp_y += k - (k + x - y) // 2
    show_xy(temp_x, temp_y)
    temp_x = x
    temp_y = y
    show_xy(temp_x, temp_y)
    return

c = (k - ((x + y) % k)) % k
if x + y < k:
    n = 2
else:
    n = math.ceil((x + y) / k) + (c % 2)

print(n)

ans = 0
temp_x = 0
temp_y = 0

temp = - (k * n - x - y) // 2
while 1:
    temp_y -= k
    if temp_y >= temp:
        show_xy(temp_x, temp_y)
    else:
        temp_x = temp - temp_y
        temp_y = temp
        #print(temp_x * a, temp_y * b)
        break

while temp_x <= x:
    show_xy(temp_x, temp_y)
    temp_x += k

temp_y += temp_x - x
temp_x = x

while temp_y <= y:
    show_xy(temp_x, temp_y)
    temp_y += k
