# @author

import sys


class ANastyaAndRice:
    def solve(self, tc=0):
        for _ in range(int(input())):
            n, a, b, c, d = [int(_) for _ in input().split()]
            if n * (a - b) > c + d or n * (a + b) < c - d:
                print("No")
            else:
                print("Yes")


solver = ANastyaAndRice()
input = sys.stdin.readline

solver.solve()
