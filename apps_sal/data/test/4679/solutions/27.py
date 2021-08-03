#
# abc045 b
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
        input = """aca
accc
ca"""
        output = """A"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abcb
aacb
bccc"""
        output = """C"""
        self.assertIO(input, output)


def resolve():
    A = list(input()) + [0]
    B = list(input()) + [0]
    C = list(input()) + [0]

    T = "a"
    while len(A) and len(B) and len(C):
        if T == "a":
            T = A.pop(0)
        elif T == "b":
            T = B.pop(0)
        else:
            T = C.pop(0)

    if len(A) == 0:
        print("A")
    elif len(B) == 0:
        print("B")
    else:
        print("C")


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
