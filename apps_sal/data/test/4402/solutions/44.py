def solver():
    (A, B) = [int(n) for n in input().split()]
    if A <= 5:
        return 0
    if 6 <= A <= 12:
        return B // 2
    if 13 <= A:
        return B


def __starting_point():
    print(solver())


__starting_point()
