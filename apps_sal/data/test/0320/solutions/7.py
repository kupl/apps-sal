n = int(input())
d = []
for i in range(0, n):
    tmp = input().split()
    (x, y) = (tmp[0], tmp[1])
    d.append((x, y))

xSum = 0
ySum = 0
for (x, y) in d:
    xSum += int(x)
    ySum += int(y)
if xSum % 2 == 0 and ySum % 2 == 0:
    print((0))
elif (xSum + ySum) % 2 == 1:
    print((-1))
else:
    result = False
    for (x, y) in d:
        if (int(x) + int(y)) % 2 == 1:
            result = True
    if result == True:
        print((1))
    else:
        print((-1))
