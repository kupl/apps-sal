x1, y1, x2, y2 = map(int, input().split())
ax = x2 - x1
ay = y2 - y1

x3 = x2 - ay
y3 = y2 + ax

x4 = x1 - ay
y4 = y1 + ax

print(x3, y3, x4, y4)
