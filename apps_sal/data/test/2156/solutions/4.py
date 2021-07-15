# @author 

import sys

class CCandies:
    def solve(self):
        n = int(input())
        s = [int(_) for _ in input().split()]
        q = int(input())
        pre = [0] * (n + 1)
        for i in range(1, n + 1):
            pre[i] = pre[i - 1] + s[i - 1]
        for i in range(q):
            li, ri = [int(_) for _ in input().split()]
            print((pre[ri] - pre[li - 1]) // 10)

solver = CCandies()
input = sys.stdin.readline

solver.solve()

