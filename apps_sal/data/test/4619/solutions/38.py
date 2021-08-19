(W, H, N) = [int(x) for x in input().split()]
x_min = 0
x_max = W
y_min = 0
y_max = H
for i in range(N):
    (x, y, a) = [int(x) for x in input().split()]
    if a == 1:
        x_min = max(x_min, x)
    elif a == 2:
        x_max = min(x_max, x)
    elif a == 3:
        y_min = max(y_min, y)
    else:
        y_max = min(y_max, y)
area = max(0, x_max - x_min) * max(0, y_max - y_min)
print(area)
