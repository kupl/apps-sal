#
# abc051 a
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
        input = """happy,newyear,enjoy"""
        output = """happy newyear enjoy"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """haiku,atcoder,tasks"""
        output = """haiku atcoder tasks"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """abcde,fghihgf,edcba"""
        output = """abcde fghihgf edcba"""
        self.assertIO(input, output)


def resolve():
    s = input()
    print((s.replace(",", " ")))


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
