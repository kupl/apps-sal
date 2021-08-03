w, h, n = map(int, input().split())
data = list(input().split() for i in range(n))
x_1 = 0
x_2 = w
y_1 = 0
y_2 = h
for i in range(n):
    if int(data[i][2]) == 1:
        if int(data[i][0]) > x_1:
            x_1 = int(data[i][0])
    elif int(data[i][2]) == 2:
        if int(data[i][0]) < x_2:
            x_2 = int(data[i][0])
    elif int(data[i][2]) == 3:
        if int(data[i][1]) > y_1:
            y_1 = int(data[i][1])
    else:
        if int(data[i][1]) < y_2:
            y_2 = int(data[i][1])
if x_2 - x_1 <= 0 or y_2 - y_1 <= 0:
    print(0)
else:
    print((x_2 - x_1) * (y_2 - y_1))
