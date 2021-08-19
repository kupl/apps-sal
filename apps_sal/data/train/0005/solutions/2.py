import sys


class BDreamoonLikesPermutations:

    def solve(self):
        for _ in range(int(input())):

            def is_perm(a):
                return len(set(a)) == len(a) and min(a) == 1 and (max(a) == len(a))
            n = int(input())
            a = [int(_) for _ in input().split()]
            done = set()
            ans = set()
            i = 0
            for i in range(n):
                if a[i] in done:
                    break
                done.add(a[i])
            if is_perm(a[:i]) and is_perm(a[i:]):
                ans.add((i, n - i))
            done = set()
            for i in range(n - 1, -1, -1):
                if a[i] in done:
                    break
                done.add(a[i])
            if is_perm(a[:i + 1]) and is_perm(a[i + 1:]):
                ans.add((i + 1, n - i - 1))
            print(len(ans))
            for sol in ans:
                print(*sol)


solver = BDreamoonLikesPermutations()
input = sys.stdin.readline
solver.solve()
