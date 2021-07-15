import unittest
import collections


def solve_b(n, m, a):
    print(a)
    b = [0]*(n+1)
    for i in range(n):
        b[i+1] = (a[i] + b[i]) % m
    print(c)
    print(b)
    cnt = 0
    for i in range(n):
        for j in range(i+1, n+1):
            if (b[j] - b[i]) % m == 0:
                cnt += 1
    return cnt


def solve(n, m, a):
    b = [0]*(n+1)
    for i in range(n):
        b[i+1] = (a[i] + b[i]) % m
    c = collections.Counter(b[1:])
    total = 0
    for k, v in list(c.items()):
        if k != 0:
            v -= 1
        if v == 0:
            continue
        total += v * (v+1)//2
    return total


def main():
    n, m = list(map(int, input().split()))
    a = list([int(x) % m for x in input().split()])
    print((solve(n, m, a)))


def __starting_point():
    main()


class Test(unittest.TestCase):
    def get_a(self, a, m):
        return list([int(x) % m for x in a.split()])

    def test1(self):
        n = 3
        m = 2
        a = self.get_a("4 1 5", m)
        expected = 3
        self.assertEqual(solve(n, m, a), expected)

    def test2(self):
        n = 13
        m = 17
        a = self.get_a("29 7 5 7 9 51 7 13 8 55 42 9 81", m)
        expected = 6
        self.assertEqual(solve(n, m, a), expected)

    def test3(self):
        n = 10
        m = 400000000
        a = self.get_a(
            "1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000 1000000000", m)
        expected = 25
        self.assertEqual(solve(n, m, a), expected)

__starting_point()
