3


def readln(): return list(map(int, input().split()))


def main():
    inp = [input() for _ in range(4)]
    a = inp[0] + inp[1][1] + inp[1][0]
    a = a.replace('X', '')
    b = inp[2] + inp[3][1] + inp[3][0]
    b = b.replace('X', '')
    print('YES' if a == b or a == b[1:] + b[0] or a == b[2] + b[:2] else 'NO')


def __starting_point():
    main()


__starting_point()
