def iroha():
    a, b, c = input().split()
    num = int(a + b + c)
    print(("YES" if num % 4 == 0 else "NO"))


def __starting_point():
    iroha()


__starting_point()
