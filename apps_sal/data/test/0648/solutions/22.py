(m, b) = input().split(' ')
m = int(m)
b = int(b)
maxx = m * b


def area(x, y):
    return (x + 1) * (y + 1) * (x + y) // 2


areas = []
i = 0
while i <= b:
    x = i * m
    y = b - i
    areas += [int(area(x, y))]
    i += 1
print(max(areas))
