def read(type=1):
    if type:
        file = open("input.dat", "r")
        line1 = list(map(int, file.readline().split()))
        line2 = list(map(int, file.readline().split()))
        line3 = list(map(int, file.readline().split()))
        file.close()
    else:
        line1 = list(map(int, input().strip().split()))
        line2 = list(map(int, input().strip().split()))
        line3 = list(map(int, input().strip().split()))
    return line1, line2, line3


def solve():
    h = a[1]
    w = a[0]
    while h > 0:
        w += h
        if h == b[1]:
            w -= b[0]
        if h == c[1]:
            w -= c[0]
        if w < 0:
            w = 0
        h -= 1
    return w


a, b, c = read(0)
sol = solve()
print(sol)
