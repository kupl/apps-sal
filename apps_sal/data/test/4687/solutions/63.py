#
# abc061 c
#
import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """3 4
1 1
2 2
3 3"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 500000
1 100000
1 100000
1 100000
1 100000
1 100000
100000 100000
100000 100000
100000 100000
100000 100000
100000 100000"""
        output = """1"""
        self.assertIO(input, output)


def resolve():
    N, K = list(map(int, input().split()))
    D = [list(map(int, input().split())) for _ in range(N)]

    D.sort()
    t = 0
    for d in D:
        t += d[1]
        if t >= K:
            print((d[0]))
            break


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
