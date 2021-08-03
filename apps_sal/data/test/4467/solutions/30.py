#
# abc091 c
#
import sys
from io import StringIO
import unittest
import bisect


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
        input = """3
2 0
3 1
1 3
4 2
0 4
5 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
0 0
1 1
5 2
2 3
3 4
4 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
2 2
3 3
0 0
1 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """5
0 0
7 3
2 2
4 8
1 6
8 5
6 9
5 4
9 1
3 7"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """5
0 0
1 1
5 5
6 6
7 7
2 2
3 3
4 4
8 8
9 9"""
        output = """4"""
        self.assertIO(input, output)


def resolve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [list(map(int, input().split())) for _ in range(N)]

    AB.sort(reverse=True)
    CD.sort()

    ans = 0
    for ab in AB:
        a, b = ab
        ok = len(CD)
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2

            if CD[mid][0] >= a:
                ok = mid
            else:
                ng = mid

        if ok == len(CD):
            continue

        NCD = CD[ok:]
        NCD.sort(key=lambda x: x[1])
        ok = len(NCD)
        ng = -1
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2

            if NCD[mid][1] >= b:
                ok = mid
            else:
                ng = mid

        if ok == len(NCD):
            continue
        else:
            ans += 1
            CD.remove(NCD[ok])

    print(ans)


def __starting_point():
    # unittest.main()
    resolve()


__starting_point()
