import sys
from io import StringIO
import unittest
from math import sqrt


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
        input = """3 2
1 2
5 5
-2 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1
2
3
4
5"""
        output = """10"""
        self.assertIO(input, output)


def resolve():
    N, D = list(map(int, input().split()))
    X = [list(map(int, input().split())) for _ in range(N)]

    ans = 0
    for i, x1 in enumerate(X):
        for x2 in X[i + 1:]:
            tmp = 0
            for j in range(D):
                tmp += (x2[j] - x1[j])**2
            tmp = sqrt(tmp)
            if tmp.is_integer() == True:
                ans += 1

    print(ans)


def __starting_point():
    resolve()


__starting_point()
