#
# abc136 c
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
        input = """5
1 2 1 1 3"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 3 2 1"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
1 2 3 4 5"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1
1000000000"""
        output = """Yes"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    H = list(map(int, input().split()))

    mx = H[0]
    ans = "Yes"
    for h in H[1:]:
        if h < mx - 1:
            ans = "No"
            break
        mx = max(mx, h)

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
