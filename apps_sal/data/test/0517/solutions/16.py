'__author__' == 'deepak Singh Mehta) '


def __starting_point():
    (n, d, h) = list(map(int, input().split()))
    if d > 2 * h or (d == 1 and n != 2):
        print(-1)
    else:
        for i in range(1, h + 1):
            print(i, i + 1)
        x = 1
        i = 1
        while i <= d - h:
            y = h + 1 + i
            print(x, y)
            x = y
            i += 1
        for i in range(d + 2, n + 1):
            print(i, 2 if d == h else 1)


__starting_point()
