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
        input = """125"""
        output = """176"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9999999999"""
        output = """12656242944"""
        self.assertIO(input, output)


def resolve():
    S = input()
    L = len(S)

    ans = 0
    for bit in range(1 << L - 1):
        s = ""
        for i in range(L):
            if 1 << i & bit:
                s += S[i]
                s += "+"
            else:
                s += S[i]
        ans += eval(s)

    print(ans)


def __starting_point():
    resolve()


__starting_point()
