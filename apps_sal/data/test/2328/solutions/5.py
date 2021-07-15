import sys
input = sys.stdin.readline


class Problem:
    def __init__(self):
        pass

    def solve(self):
        self._solve()

    def _solve(self):
        t = int(input())
        for _ in range(t):
            n, k = [int(item) for item in input().split()]
            a = [int(item) for item in input().split()]
            a.sort()
            mn = float('inf')
            idx = -1
            for i in range(n - k):
                if a[i + k] - a[i] < mn:
                    mn = a[i + k] - a[i]
                    idx = i
            print((a[idx] + a[idx + k]) >> 1)


def main():
    problem = Problem()
    problem.solve()


def __starting_point():
    main()

__starting_point()
