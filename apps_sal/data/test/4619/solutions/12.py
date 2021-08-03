w, h, n = list(map(int, input().split()))
x_pos = [0, w]
y_pos = [0, h]
for _ in range(n):
    x, y, a = list(map(int, input().split()))
    if a == 1:
        x_pos[0] = max(x_pos[0], x)
    elif a == 2:
        x_pos[1] = min(x_pos[1], x)
    elif a == 3:
        y_pos[0] = max(y_pos[0], y)
    else:
        y_pos[1] = min(y_pos[1], y)
ans = max(0, (x_pos[1] - x_pos[0])) * max(0, (y_pos[1] - y_pos[0]))
print(ans)
