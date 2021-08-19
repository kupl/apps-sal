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
        input = '1 21'
        output = 'Yes'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '100 100'
        output = 'No'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '12 10'
        output = 'No'
        self.assertIO(input, output)


def resolve():
    (A, B) = input().split()
    C = int(A + B)
    for i in range(1, 100100):
        if i ** 2 == C:
            print('Yes')
            break
    else:
        print('No')


def __starting_point():
    resolve()


__starting_point()
