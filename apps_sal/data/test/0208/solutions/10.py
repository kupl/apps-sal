def process(x1, y1, x2, y2):
    if x1 == x2:
        print('{0} {1} {0} {2}'.format(x1 + abs(y2 - y1), y1, y2))
    elif y1 == y2:
        print('{1} {0} {2} {0}'.format(y1 + abs(x2 - x1), x1, x2))
    elif abs(y2 - y1) == abs(x2 - x1):
        print('{0} {3} {2} {1}'.format(x1, y1, x2, y2))
    else:
        print(-1)


def __starting_point():
    process(*(int(i) for i in input().split(' ')))


__starting_point()
