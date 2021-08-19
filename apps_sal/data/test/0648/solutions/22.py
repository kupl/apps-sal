m, b = input().split(" ")
m = int(m)
b = int(b)

maxx = m * b

# def solvefory(x):
# nonlocal m, b
##    m1 = 1/m
##    y = -1 * x * m1 + b
# return y


def area(x, y):
    return ((x + 1) * (y + 1) * (x + y)) // 2


areas = []
##xy = []
i = 0
while i <= b:
    ##    xy += [[i, solvefory(i)], ]
    x = i * m
    y = b - i
    areas += [int(area(x, y)), ]
    i += 1
print(max(areas))
# print(xy)
