from itertools import product, takewhile


def main():
    words = ['eraser', 'erase', 'dreamer', 'dream']
    S = input()[::-1]
    for word in words:
        S = S.replace(word[::-1], '')
    if len(S) > 0:
        print('NO')
    else:
        print('YES')


def __starting_point():
    main()


__starting_point()
