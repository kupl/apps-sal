def iroha():
    x, a, b = list(map(int, input().split()))
    on = abs(x - a)
    off = abs(x - b)
    print(("A" if on < off else "B"))


def __starting_point():
    iroha()


__starting_point()
