def solver():
    (A, P) = [int(n) for n in input().split()]
    return (A * 3 + P) // 2


def __starting_point():
    print(solver())


__starting_point()
