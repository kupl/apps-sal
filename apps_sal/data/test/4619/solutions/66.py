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
        input = '5 4 2\n2 1 1\n3 3 4'
        output = '9'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '5 4 3\n2 1 1\n3 3 4\n1 4 2'
        output = '0'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '10 10 5\n1 6 1\n4 1 3\n6 9 4\n9 4 2\n3 1 3'
        output = '64'
        self.assertIO(input, output)


def resolve():
    (W, H, N) = list(map(int, input().split()))
    a = []
    ox = 0
    oy = 0
    for _ in range(N):
        a.append(list(map(int, input().split())))
    for i in range(N):
        if a[i][2] == 1:
            ox = max(a[i][0], ox)
        elif a[i][2] == 2:
            W = min(a[i][0], W)
        elif a[i][2] == 3:
            oy = max(a[i][1], oy)
        elif a[i][2] == 4:
            H = min(a[i][1], H)
    print(max(W - ox, 0) * max(H - oy, 0))


def __starting_point():
    resolve()


__starting_point()
