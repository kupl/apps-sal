
def read(t=int):
    return t(input())


def read_arr(t=int):
    return [t(i) for i in str(input()).split()]


t = 1
for i in range(t):
    x1, y1 = read_arr()
    x2, y2 = read_arr()
    x3, y3 = read_arr()

    print(3)
    print(x1 + x2 - x3, y1 + y2 - y3)
    print(x2 + x3 - x1, y2 + y3 - y1)
    print(x3 + x1 - x2, y3 + y1 - y2)
