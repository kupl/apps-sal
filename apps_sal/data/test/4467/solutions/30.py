import sys
from io import StringIO
import unittest
import bisect


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
        input = '3\n2 0\n3 1\n1 3\n4 2\n0 4\n5 5'
        output = '2'
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = '3\n0 0\n1 1\n5 2\n2 3\n3 4\n4 5'
        output = '2'
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = '2\n2 2\n3 3\n0 0\n1 1'
        output = '0'
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = '5\n0 0\n7 3\n2 2\n4 8\n1 6\n8 5\n6 9\n5 4\n9 1\n3 7'
        output = '5'
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = '5\n0 0\n1 1\n5 5\n6 6\n7 7\n2 2\n3 3\n4 4\n8 8\n9 9'
        output = '4'
        self.assertIO(input, output)


def resolve():
    N = int(input())
    AB = [list(map(int, input().split())) for _ in range(N)]
    CD = [list(map(int, input().split())) for _ in range(N)]
    AB.sort(reverse=True)
    CD.sort()
    ans = 0
    for ab in AB:
        (a, b) = ab
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
    resolve()


__starting_point()
