w, h, n = map(int, input().split())
x1 = [0]  # 1 left border of white area
x2 = [w]  # 2
y1 = [0]  # 3
y2 = [h]  # 4
for i in range(n):
    x, y, a = map(int, input().split())
    if a == 1:
        x1.append(x)
    elif a == 2:
        x2.append(x)
    elif a == 3:
        y1.append(y)
    elif a == 4:
        y2.append(y)

left = max(x1)
right = min(x2)
bottom = max(y1)
top = min(y2)


ans = max(0, right - left) * max(0, top - bottom)

print(ans)
