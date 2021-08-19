def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(' '))


def check(i, j, s):
    bomb = 0
    for (x, y) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1), (i + 1, j + 1)]:
        if s[x][y] == '#':
            bomb += 1
    return str(bomb)


def main():
    (h, w) = Input()
    p = ['x'] * (w + 2)
    s = [p] + [['x'] + list(input()) + ['x'] for i in range(h)] + [p]
    for i in range(1, h + 1):
        ans = ''
        for j in range(1, w + 1):
            if s[i][j] == '.':
                ans += check(i, j, s)
            else:
                ans += '#'
        print(ans)


main()
