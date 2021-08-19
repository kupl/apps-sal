import sys


class APaintTheNumbers:

    def solve(self):
        n = int(input())
        a = [int(_) for _ in input().split()]
        a.sort()
        ans = 0
        done = [0] * n
        for i in range(n):
            if done[i]:
                continue
            ans += 1
            for j in range(i, n):
                if done[j]:
                    continue
                if a[j] % a[i] == 0:
                    done[j] = 1
        print(ans)


solver = APaintTheNumbers()
input = sys.stdin.readline
solver.solve()
