#
# abc157 c
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
        input = """3 3
1 7
3 2
1 7"""
        output = """702"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
2 1
2 3"""
        output = """-1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1
1 0"""
        output = """-1"""
        self.assertIO(input, output)


def resolve():
    N, M = list(map(int, input().split()))
    SC = [list(map(int, input().split())) for _ in range(M)]
    SC = set(map(tuple, SC))
    SC = list(set(SC))
    SC.sort()

    ans = -1
    for i in range(10**N):
        si = str(i)
        if len(si) != N:
            continue
        for sc in SC:
            s, c = sc
            if si[s-1] != str(c):
                break
        else:
            ans = i
            break

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
