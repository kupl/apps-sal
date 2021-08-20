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
        input = '3\n1\n2 1\n1\n1 1\n1\n2 0'
        output = '2'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3\n2\n2 1\n3 0\n2\n3 1\n1 0\n2\n1 1\n2 0'
        output = '0'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '2\n1\n2 0\n1\n1 0'
        output = '1'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    C = []
    for i in range(N):
        a = int(input())
        C.append([list(map(int, input().split())) for j in range(a)])
    ans = 0
    for bit in range(1 << N):
        t = 0
        for i in range(N):
            if bit & 1 << i:
                for c in C[i]:
                    if bit & 1 << c[0] - 1 != (1 << c[0] - 1) * c[1]:
                        break
                else:
                    t += 1
        if t == bin(bit).count('1'):
            ans = max(ans, t)
    print(ans)


def __starting_point():
    resolve()


__starting_point()
