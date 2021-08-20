import sys
input = sys.stdin.readline


class Problem:

    def __init__(self):
        pass

    def solve(self):
        print(self._solve())

    def _solve(self):
        (n, a, x, b, y) = [int(item) for item in input().split()]
        a -= 1
        b -= 1
        x -= 1
        y -= 1
        if a == b:
            return 'YES'
        for i in range(n):
            a = (a + 1) % n
            b = (b - 1) % n
            if a == b:
                return 'YES'
            if b == y or a == x:
                break
        return 'NO'


def main():
    problem = Problem()
    problem.solve()


def __starting_point():
    main()


__starting_point()
