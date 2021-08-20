import sys
import io
from collections import Counter


def solve(n, vs):
    assert 2 <= n <= 1000
    for v in vs:
        assert 1 <= v <= 1000
    (lv, rvs) = (vs[0], vs[1:])
    cnt = 0
    votes = Counter(rvs)
    max_vote = max(rvs)
    while lv <= max_vote:
        votes[max_vote] -= 1
        votes[max_vote - 1] += 1
        if votes[max_vote] == 0:
            max_vote -= 1
        lv += 1
        cnt += 1
    return cnt


def getinput():

    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    return [getint(), getints_line()]


def iosolve():
    return str(solve(*getinput()))


def main():
    if sys.stdin.isatty():
        test()
    stdin_lines = getstdin_lines()
    sys.stdin = io.StringIO('\n'.join(stdin_lines))
    if stdin_lines:
        print(iosolve())
    else:
        test()


def test():
    IO_TEST_CASES = [('5\n5 1 11 2 8\n            ', '4\n            '), ('4\n1 8 8 8\n            ', '6\n            '), ('2\n7 6\n            ', '0\n            ')]
    TEST_CASES = []
    import unittest
    import sys
    import io

    class Assert(unittest.TestCase):

        def equal(self, a, b):
            self.assertEqual(a, b)

        def float_equal(self, actual, expect, tolerance):
            self.assertTrue(expect - tolerance < actual < expect + tolerance)
    art = Assert()
    for (inputs, expect) in TEST_CASES:
        art.equal(solve(*inputs), expect)
    for (stdin, expect) in IO_TEST_CASES:
        sys.stdin = io.StringIO(stdin.strip())
        art.equal(iosolve(), expect.strip())


def getstdin_lines():
    stdin = []
    while 1:
        try:
            stdin.append(input())
        except EOFError:
            break
    return stdin


def __starting_point():
    main()


__starting_point()
