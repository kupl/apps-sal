
data = input().split(" ")
a = int(data[0])
b = int(data[1])
c = int(data[2])

x = 0
y = 0
z = 0

if (a - b + c) % 2 != 0:
    print("Impossible")
else:
    z = int((a - b + c) / 2)
    x = int(a - z)
    y = int(b - x)

    if (x == y == 0) or (x == z == 0) or (z == y == 0):
        print("Impossible")
    elif min(x, y, z) >= 0:
        print("%s %s %s" % (x, y, z))
    else:
        print("Impossible")
