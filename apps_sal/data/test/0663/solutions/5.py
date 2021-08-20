import math
line = input().split()
r = int(line[0])
x0 = int(line[1])
y0 = int(line[2])
x1 = int(line[3])
y1 = int(line[4])
while True:
    if x0 == x1 and y0 == y1:
        print('0')
        break
    dist = ((x1 - x0) ** 2 + (y1 - y0) ** 2) ** (1 / 2)
    print(str(math.ceil(dist / (2 * r))))
    break
