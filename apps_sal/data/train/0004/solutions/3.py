import sys


class BBeautifulNumbers:

    def solve(self):
        for _ in range(int(input())):
            n = int(input())
            p = [int(_) - 1 for _ in input().split()]
            mn_index = [float('inf')] * n
            mx_index = [-float('inf')] * n
            prev = [0] * n
            for i in range(n):
                prev[p[i]] = i
            for i in range(n):
                mn_index[i] = min(mn_index[i - 1], prev[i])
                mx_index[i] = max(mx_index[i - 1], prev[i])
            ans = ['0'] * n
            for i in range(n):
                (l, r) = (mn_index[i], mx_index[i])
                ans[i] = '1' if r - l + 1 == i + 1 else '0'
            print(''.join(ans))


solver = BBeautifulNumbers()
input = sys.stdin.readline
solver.solve()
