#
# abc104 b
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
        input = """AtCoder"""
        output = """AC"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """ACoder"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """AcycliC"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """AtCoCo"""
        output = """WA"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """Atcoder"""
        output = """WA"""
        self.assertIO(input, output)


def resolve():
    S = input()

    l = len(S)
    ans = "AC"
    cf = False
    for i in range(l):
        if i == 0:
            if S[i] != "A":
                ans = "WA"
                break
        elif i == 1 or i == l - 1:
            if S[i] == "C" or S[i].isupper():
                ans = "WA"
                break
        else:
            if S[i] == "C":
                if cf == True:
                    ans = "WA"
                    break
                else:
                    cf = True
            elif S[i].isupper():
                ans = "WA"
                break
    else:
        if cf == False:
            ans = "WA"

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
