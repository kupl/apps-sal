import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):

    def assertIO(self, input, output):
        (stdout, stdin) = (sys.stdout, sys.stdin)
        (sys.stdout, sys.stdin) = (StringIO(), StringIO(input))
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        (sys.stdout, sys.stdin) = (stdout, stdin)
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = '3\n2 3\n1 1\n3 2'
        output = '10'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '4\n1 1\n1 1\n1 5\n1 100'
        output = '101'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '5\n3 10\n48 17\n31 199\n231 23\n3 2'
        output = '6930'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    R = [list(map(int, input().split())) for _ in range(N)]
    t = R[0][0]
    a = R[0][1]
    for i in range(1, N):
        n = max((t + R[i][0] - 1) // R[i][0], (a + R[i][1] - 1) // R[i][1])
        t = n * R[i][0]
        a = n * R[i][1]
    print(t + a)


def __starting_point():
    resolve()


__starting_point()
