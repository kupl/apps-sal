
import sys


class ADIYWoodenLadder:
    def solve(self):
        t = int(input())
        for _ in range(t):
            n = int(input())
            a = [int(_) for _ in input().split()]
            a.sort()
            print(min(a[-2] - 1, n - 2))


solver = ADIYWoodenLadder()
input = sys.stdin.readline

solver.solve()
