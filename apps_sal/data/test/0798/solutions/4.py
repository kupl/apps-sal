a, b, c = list(map(int, input().split()))

x = (a + b - c) // 2
y = (b + c - a) // 2
z = (a + c - b) // 2

if x < 0 or y < 0 or z < 0 or (a + b + c) % 2 != 0:
    print("Impossible")
else:
    print("{} {} {}".format(x, y, z))
