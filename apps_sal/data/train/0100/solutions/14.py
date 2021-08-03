a = int(input())
for i in range(a):
    x, y, z = map(int, input().split())
    x, y, z = sorted([x, y, z])
    k = z - y
    if k == 0:
        y += x // 2
        print(y)
    elif k > x:
        y += x
        print(y)
    else:
        x -= z - y
        y = z
        z += x // 2
        print(z)
