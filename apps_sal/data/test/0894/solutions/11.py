3
(x, y) = tuple(map(int, input().split()))
if x > 0 and y > 0:
    print(0, x + y, x + y, 0)
elif x > 0 and y < 0:
    print(0, -x + y, x - y, 0)
elif x < 0 and y > 0:
    print(x - y, 0, 0, -x + y)
else:
    print(x + y, 0, 0, x + y)
