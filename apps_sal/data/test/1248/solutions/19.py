def solve(d1, d2, d3):

    return min(2 * d1 + 2 * d2, d1 + d2 + d3, 2 * (d1 + d3), 2 * (d2 + d3))


def __starting_point():

    d1, d2, d3 = [int(x) for x in input().split()]
    print(solve(d1, d2, d3))


__starting_point()
