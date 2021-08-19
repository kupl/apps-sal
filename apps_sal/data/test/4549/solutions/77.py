def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def check(i, j, data):
    return any((data[x][y] == '#' for (x, y) in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1))))


def main():
    (h, w) = Input()
    a = ['-' * (w + 2)]
    data = a + ['-' + input() + '-' for _ in range(h)] + a
    ans = True
    for i in range(1, h + 1):
        for j in range(1, w + 1):
            if data[i][j] == '#':
                if not check(i, j, data):
                    ans = False
    if ans:
        print('Yes')
    else:
        print('No')


main()
