# @author

import sys


class BNumberCircle:
    def solve(self):
        n = int(input())
        a = [int(_) for _ in input().split()]
        a.sort()
        if a[-1] >= a[-2] + a[-3]:
            print("NO")
        else:
            print("YES")
            ans = [-1] * n
            cur = 0
            i = n - 1
            while i >= 0:
                ans[cur] = a[i]
                cur = n - 1 - cur
                i -= 1
                if i < 0:
                    break
                ans[cur] = a[i]
                cur = n - 1 - cur + 1
                i -= 1

            print(*ans)


solver = BNumberCircle()
input = sys.stdin.readline

solver.solve()
