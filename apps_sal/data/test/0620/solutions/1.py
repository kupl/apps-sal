points = []
for i in range(3):
    points.append(list(map(int, input().split())))


def get4(a, b, c):
    return [b[0] + c[0] - a[0], b[1] + c[1] - a[1]]


print(3)
for i in range(3):
    points = points[1:] + [points[0]]
    print(' '.join(map(str, get4(*points))))
