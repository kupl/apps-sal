(x_1, y_1) = input().split()
(x_2, y_2) = input().split()
x_1 = int(x_1)
x_2 = int(x_2)
y_1 = int(y_1)
y_2 = int(y_2)
if x_1 == x_2:
    jwb = 2 * (abs(y_2 - y_1) + 1) + 4
elif y_1 == y_2:
    jwb = 2 * (abs(x_2 - x_1) + 1) + 4
else:
    jwb = 2 * (abs(x_2 - x_1) + 1) + 2 * (abs(y_2 - y_1) + 1)
print(jwb)
