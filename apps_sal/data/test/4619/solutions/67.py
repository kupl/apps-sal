w, h, n = map(int, input().split())
x_pos = [0, w]
y_pos = [0, h]
for _ in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        x_pos[0] = max(x_pos[0], x)
    elif a == 2:
        x_pos[1] = min(x_pos[1], x)
    elif a == 3:
        y_pos[0] = max(y_pos[0], y)
    else:
        y_pos[1] = min(y_pos[1], y)
if x_pos[1] - x_pos[0] < 0 or y_pos[1] - y_pos[0] < 0:
    ans = 0
else:
    ans = (x_pos[1] - x_pos[0] ) * (y_pos[1] - y_pos[0])
print(ans)
