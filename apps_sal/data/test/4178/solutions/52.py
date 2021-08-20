def main():
    n = int(input())
    h = list(map(int, input().split()))
    f = True
    for i in reversed(range(n - 1)):
        if h[i] - 1 > h[i + 1]:
            f = False
        elif h[i] - 1 == h[i + 1]:
            h[i] -= 1
    if f:
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
