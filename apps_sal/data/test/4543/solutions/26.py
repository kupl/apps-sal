def resolve():
    from math import sqrt

    n = int("".join(input().split()))
    print("Yes" if n == int(sqrt(n)) ** 2 else "No")


def __starting_point():
    resolve()


__starting_point()
