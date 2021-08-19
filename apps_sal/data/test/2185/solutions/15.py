import sys


class ASinglePush:

    def solve(self):
        t = int(input())
        for _ in range(t):
            n = int(input())
            a = [int(_) for _ in input().split()]
            b = [int(_) for _ in input().split()]
            u = [b[i] - a[i] for i in range(n)]
            l = -1
            r = -1
            for i in range(n):
                if u[i]:
                    l = i
                    break
            for i in range(n - 1, -1, -1):
                if u[i]:
                    r = i
                    break
            if l == -1:
                print('YES')
            else:
                assert l != -1 and r != -1
                print('YES' if u[l] > 0 and u[l:r + 1] == [u[l]] * (r - l + 1) else 'NO')


solver = ASinglePush()
input = sys.stdin.readline
solver.solve()
