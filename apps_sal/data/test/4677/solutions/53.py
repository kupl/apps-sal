import sys


def solve(s: str):
    a = []
    for c in s:
        if c == "B":
            if a:
                a.pop()
        else:
            a.append(c)
    return "".join(a)


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)
    print((solve(s)))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    main()


__starting_point()
