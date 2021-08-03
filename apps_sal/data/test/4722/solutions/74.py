def iroha():
    a, b = map(int, input().split())
    aa = a % 3
    bb = b % 3
    cc = (a + b) % 3

    print("Possible") if aa == 0 or bb == 0 or cc == 0 else print("Impossible")


def __starting_point():
    iroha()


__starting_point()
