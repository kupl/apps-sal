

def main():
    import sys
    input = sys.stdin.readline

    n, m = list(map(int, input().split()))
    first = list()
    second = list()

    for i in range(m):
        ai, bi = list(map(int, input().split()))

        if ai == 1:
            first.append(bi)

        if bi == n:
            second.append(ai)

    ans = set(first) & set(second)

    if len(ans) > 0:
        print('POSSIBLE')
    else:
        print('IMPOSSIBLE')


def __starting_point():
    main()


__starting_point()
