#
# abc145 b
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
        input = """6
abcabc"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6
abcadc"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1
z"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    S = input()

    ans = "No"
    if N % 2 == 0 and S[:N//2] == S[N//2:]:
        ans = "Yes"

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
