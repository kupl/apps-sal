import sys


def solve(s: str, t: str):
    """
    >>> solve("aaa", "aaa")
    3
    >>> solve("a", "a")
    1
    >>> solve("contest", "son")
    10
    """
    from collections import defaultdict
    from bisect import bisect
    d = defaultdict(list)
    for (i, c) in enumerate(s):
        d[c].append(i)
    (ans, i) = (0, -1)
    for c in t:
        if not d[c]:
            return -1
        j = bisect(d[c], i)
        if len(d[c]) == j:
            ans += len(s) - i + d[c][0]
            i = d[c][0]
        else:
            ans += d[c][j] - i
            i = d[c][j]
    return ans


def main():

    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    s = next(tokens)
    t = next(tokens)
    print(solve(s, t))


def test():
    import doctest
    doctest.testmod()


def __starting_point():
    test()
    main()


__starting_point()
