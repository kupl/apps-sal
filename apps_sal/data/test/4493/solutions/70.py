import sys

YES = "Yes"
NO = "No"


def solve(c: "List[List[int]]"):
    from itertools import product
    for a1, b1 in product(list(range(101)), repeat=2):
        a2 = c[1][0] - b1
        a3 = c[2][0] - b1
        b2 = c[0][1] - a1
        b3 = c[0][2] - a1
        if a2 < 0 or a3 < 0 or b2 < 0 or b3 < 0:
            continue
        a = [a1, a2, a3]
        b = [b1, b2, b3]
        if all((a[i] + b[j]) == c[i][j] for i, j in product(list(range(3)), repeat=2)):
            return YES
    return NO


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    c = [[int(next(tokens)) for _ in range(3)] for _ in range(3)]
    print((solve(c)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
