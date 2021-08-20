def readinput():
    (t, x) = list(map(int, input().split()))
    return (t, x)


def main(t, x):
    return t / x


def __starting_point():
    (t, x) = readinput()
    ans = main(t, x)
    print(ans)


__starting_point()
