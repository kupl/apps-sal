a = [int(i) for i in input().split()]
x1 = a[0]
y1 = a[1]
x2 = a[2]
y2 = a[3]
l = 0
if(x1 == x2):
    l = abs(y1 - y2)
    print(x1 + l, y1, x1 + l, y2)
elif(y1 == y2):
    l = abs(x1 - x2)
    print(x1, y1 + l, x2, y1 + l)
elif(abs(x1 - x2) == abs(y1 - y2)):
    print(x2, y1, x1, y2)
else:
    print(-1)
