import sys
import io
from collections import defaultdict
from itertools import combinations


def solve(n, m, pairs):
    assert 3 <= n <= 4000
    assert 0 <= m <= 4000
    recognitions = defaultdict(set)
    for (a, b) in pairs:
        recognitions[a].add(b)
        recognitions[b].add(a)
    minr = float('inf')
    for (candidate, recognition) in [(c, rs) for (c, rs) in list(recognitions.items()) if len(rs) > 1]:
        for (c2, c3) in [(a, b) for (a, b) in combinations(recognition, 2) if a in recognitions[b]]:
            sum_r = sum([len(recognitions[x]) for x in [candidate, c2, c3]])
            minr = min([sum_r, minr])
    if minr == float('inf'):
        return -1
    else:
        return minr - 2 * 3


def getinput():

    def getint():
        return int(input())

    def getints_line():
        return list(map(int, input().split(' ')))

    def getints(n):
        return [getint() for _ in range(n)]

    def getints_lines(n):
        return [getints_line() for _ in range(n)]
    (n, m) = getints_line()
    return [n, m, getints_lines(m)]


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
    IO_TEST_CASES = [('5 6\n1 2\n1 3\n2 3\n2 4\n3 4\n4 5\n            ', '2\n            '), ('7 4\n2 1\n3 6\n5 1\n1 7\n            ', '-1\n            ')]
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
