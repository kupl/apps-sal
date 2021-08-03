#
# abc064 c
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
        input = """4
2100 2500 2700 2700"""
        output = """2 2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
1100 1900 2800 3200 3200"""
        output = """3 5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """20
800 810 820 830 840 850 860 870 880 890 900 910 920 930 940 950 960 970 980 990"""
        output = """1 1"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    A = list(map(int, input().split()))

    C = [0] * 9
    for a in A:
        for i in range(8):
            if 400 * i <= a <= 400 * i + 399:
                C[i] = 1
                break
        else:
            C[8] += 1

    print(f"{max(1, C[:8].count(1))} {C[:8].count(1)+C[8]}")


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
