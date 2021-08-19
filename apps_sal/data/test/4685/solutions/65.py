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
        input = '5 3 11\n1'
        output = '30'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3 3 4\n2'
        output = '22'
        self.assertIO(input, output)


def resolve():
    I = list(map(int, input().split()))
    K = int(input())
    for i in range(K):
        t = max(I)
        I.remove(t)
        I.append(t * 2)
    print(sum(I))


def __starting_point():
    resolve()


__starting_point()
