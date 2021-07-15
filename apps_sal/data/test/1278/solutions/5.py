# @author 

import sys

class ACityDay:
    def solve(self):
        n, x, y = [int(_) for _ in input().split()]
        a = [int(_) for _ in input().split()]
        for d in range(n):
            ok = True
            for j in range(d - x, d + y + 1):
                if j == d or j < 0 or j >= n:
                    continue
                if a[j] <= a[d]:
                    ok = False
                    break

            if ok:
                print(d + 1)
                break


solver = ACityDay()
input = sys.stdin.readline

solver.solve()

