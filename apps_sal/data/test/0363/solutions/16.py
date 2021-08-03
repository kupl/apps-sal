def xxx(n):
    total = 0
    curr = 9
    for i in range(n):
        total += curr * (i + 1)
        curr *= 10

    return total


def __starting_point():
    n = int(input())
    l = len(str(n))
    a = xxx(l - 1)
    b = (n - 10 ** (l - 1) + 1) * l
    print(a + b)


__starting_point()
