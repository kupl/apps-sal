#
# abc042 c
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
        input = """1000 8
1 3 4 5 6 7 8 9"""
        output = """2000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999 1
0"""
        output = """9999"""
        self.assertIO(input, output)


def resolve():
    N, K = list(map(int, input().split()))
    D = list(input().split())

    for i in range(N, 10 * N + 1):
        for d in D:
            if str(i).count(d) != 0:
                break
        else:
            print(i)
            break


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
