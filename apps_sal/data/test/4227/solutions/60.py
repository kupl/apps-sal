import sys
from io import StringIO
import unittest
import itertools


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
        input = '3 3\n1 2\n1 3\n2 3'
        output = '2'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '7 7\n1 3\n2 7\n3 4\n4 5\n4 6\n5 6\n6 7'
        output = '1'
        self.assertIO(input, output)


def resolve():
    (N, M) = list(map(int, input().split()))
    P = [list(map(int, input().split())) for _ in range(M)]
    R = itertools.permutations(list(range(1, N + 1)))
    ans = 0
    for r in R:
        flag = True
        r = list(r)
        if r[0] != 1:
            break
        for i in range(1, N):
            for p in P:
                if r[i - 1] == p[0] and r[i] == p[1] or (r[i - 1] == p[1] and r[i] == p[0]):
                    break
            else:
                flag = False
        if flag == True:
            ans += 1
    print(ans)


def __starting_point():
    resolve()


__starting_point()
