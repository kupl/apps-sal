import sys


class Solution:
    def largestComponentSize(self, a: List[int]) -> int:
        sys.setrecursionlimit(9000000)

        def unify(x: int, y: int):
            f1 = getfa(x)
            f2 = getfa(y)
            if f1 != f2:
                if fa[f1] < fa[f2]:
                    fa[f1] += fa[f2]
                    fa[f2] = f1
                else:
                    fa[f2] += fa[f1]
                    fa[f1] = f2

        def getfa(x: int) -> int:
            i = x
            while fa[i] >= 0:
                i = fa[i]

            j = i
            i = x
            while fa[i] >= 0:
                fa[i], i = j, fa[i]

            return j

        n = len(a)
        flag = dict()
        fa = [-1] * n
        ans = 1

        for i in range(0, n):
            v = a[i]
            if v % 2 == 0:
                if 2 not in flag:
                    flag[2] = i
                else:
                    unify(flag[2], i)
                while v % 2 == 0:
                    v >>= 1

            j = 3
            lim = int(sqrt(v)) + 1

            while j <= lim and j <= v:
                if v % j:
                    j += 2
                    continue

                if j not in flag:
                    flag[j] = i
                else:
                    unify(flag[j], i)

                while v % j == 0:
                    v //= j
                j += 2

            if v > 1:
                if v not in flag:
                    flag[v] = i
                else:
                    unify(flag[v], i)

        for i in range(0, n):
            if fa[i] < 0:
                ans = max(ans, -fa[i])

        return ans
