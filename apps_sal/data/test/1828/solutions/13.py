n = int(input())
counter = 0
direction = 0
input()
x_0, y_0 = list(map(int, input().split()))
for i in range(n - 1):
    x_1, y_1 = list(map(int, input().split()))
    if direction == 0:
        if x_1 < x_0:
            counter += 1
    elif direction == 1:
        if y_1 > y_0:
            counter += 1
    elif direction == 2:
        if x_0 < x_1:
            counter += 1
    elif direction == 3:
        if y_1 < y_0:
            counter += 1
    if direction == 0 or direction == 2:
        if x_1 < x_0:
            direction = 3
        else:
            direction = 1
    else:
        if y_1 > y_0:
            direction = 0
        else:
            direction = 2
    x_0, y_0 = x_1, y_1
print(counter)

