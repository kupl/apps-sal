#
# abc054 b
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
        input = """3 2
#.#
.#.
#.#
#.
.#"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 1
....
....
....
....
#"""
        output = """No"""
        self.assertIO(input, output)


def resolve():
    N, M = list(map(int, input().split()))
    A = [list(input()) for _ in range(N)]
    B = [list(input()) for _ in range(M)]

    ans = "No"
    for i in range(N-M+1):
        for j in range(N-M+1):
            ans = "Yes"
            for k in range(M):
                if ans == "No":
                    break
                for l in range(M):
                    if A[i+k][j+l] != B[k][l]:
                        ans = "No"
                        break
            if ans == "Yes":
                break
        if ans == "Yes":
            break

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()

__starting_point()
