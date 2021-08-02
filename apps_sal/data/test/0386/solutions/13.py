__author__ = 'Lipen'


def ModeReverse(mode):
    if mode == '>':
        return '<='
    elif mode == '<':
        return '>='
    elif mode == '>=':
        return '<'
    elif mode == '<=':
        return '>'


def main():
    n = int(input())
    ymin = -2000000000
    ymax = 2000000000

    for i in range(n):
        mode, x, ans = input().split()
        x = int(x)

        if ans == 'N':
            mode = ModeReverse(mode)

        if mode == '>':
            ymin = max(ymin, x + 1)
        elif mode == '<':
            ymax = min(ymax, x - 1)
        elif mode == '>=':
            ymin = max(ymin, x)
        elif mode == '<=':
            ymax = min(ymax, x)

    if ymin > ymax:
        print('Impossible')
    else:
        print(ymin)


main()
