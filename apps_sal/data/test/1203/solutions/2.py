import sys


class BWaterLily:

    def solve(self):
        (h, l) = [int(_) for _ in input().split()]
        print((l ** 2 - h ** 2) / (2 * h))


solver = BWaterLily()
input = sys.stdin.readline
solver.solve()
