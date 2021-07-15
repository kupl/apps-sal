x1,y1,x2,y2 = list(map(int, input().split()))


dx = y1 - y2
dy = x2 - x1

x3 = x2 + dx
y3 = y2 + dy

x4 = x3 + (x1-x2)
y4 = y3 + (y1-y2)

print(("{} {} {} {}".format(x3,y3, x4, y4)))


