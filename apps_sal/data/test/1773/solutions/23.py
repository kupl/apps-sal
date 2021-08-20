"""
Lala Land has exactly n apple trees
Tree number i is located in a position xi and has ai apples growing on it

Obj: wants to collect apples from the apple trees
Start: Amr currently stands in x\u2009=\u20090 position
"""


def solve(n, xas):
    minus = sorted([xa for xa in xas if xa[0] < 0])
    minus_len = len(minus)
    plus = sorted([xa for xa in xas if xa[0] > 0])
    plus_len = len(plus)
    d = abs(minus_len - plus_len)
    if d < 2:
        pass
    elif minus_len < plus_len:
        plus = plus[:-(d - 1)]
    else:
        minus = minus[d - 1:]
    return sum([x[1] for x in minus]) + sum([x[1] for x in plus])


def getinput():

    def getints_line():
        return list(map(int, input().split(' ')))
    n = int(input())
    xas = [getints_line() for _ in range(n)]
    return (n, xas)


def test():
    assert solve(2, [[-1, 5], [1, 5]]) == 10
    assert solve(3, [[-2, 2], [1, 4], [-1, 3]]) == 9
    assert solve(3, [[1, 9], [3, 5], [7, 10]]) == 9


def main():
    print(solve(*getinput()))


def __starting_point():
    main()


__starting_point()
