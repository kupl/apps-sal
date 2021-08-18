
import sys


class AShortSubstrings:
    def solve(self, tc=0):
        for _ in range(int(input())):
            b = input().strip()
            print(''.join(b[i] for i in range(len(b)) if i % 2 == 0) + b[-1])


solver = AShortSubstrings()
input = sys.stdin.readline

solver.solve()
