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
        input = """ant
obe
rec"""
        output = """abc"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """edu
cat
ion"""
        output = """ean"""
        self.assertIO(input, output)


def resolve():
    C1 = input()
    C2 = input()
    C3 = input()

    print((C1[0] + C2[1] + C3[2]))


def __starting_point():
    resolve()


__starting_point()
