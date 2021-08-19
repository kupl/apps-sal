def getval():
    n = int(input())
    x = list(map(int, input().split()))
    return (n, x)


def main(n, x):
    y = sorted(x)
    (a, b) = (y[(n - 1) // 2], y[(n - 1) // 2 + 1])
    for i in x:
        if i > a:
            print(a)
        else:
            print(b)


def __starting_point():
    (n, x) = getval()
    main(n, x)


__starting_point()
