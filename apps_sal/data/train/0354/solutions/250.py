class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        if n == 0:
            return 0

        memo = {}

        def f(d, r, n):
            if n == 1:
                return 1

            if (d, r, n) in memo:
                return memo[(d, r, n)]

            total = 0
            for nd in range(6):
                if nd != d:
                    total += f(nd, 1, n - 1)
            if r < rollMax[d]:
                total += f(d, r + 1, n - 1)

            memo[(d, r, n)] = total
            return total % (10**9 + 7)

        total = 0
        for d in range(6):
            total += f(d, 1, n)
        return total % (10**9 + 7)

        f = [None] * n
        for i in range(0, n):
            f[i] = [None] * 6
            for d in range(6):
                if i == 0:
                    f[i][d] = [1] * rollMax[d]
                    continue

                f[i][d] = [0] * rollMax[d]
                for r in range(rollMax[d]):
                    f[i][d][r] += f[i - 1][d][r - 1] if r - 1 >= 0 else 0

                for r in range(rollMax[d]):
                    for nd in range(6):
                        if nd != d:
                            f[i][d][r] += f[i - 1][nd][0]

        total = 0
        for d in range(len(f[n - 1])):
            total += f[n - 1][d][rollMax[d] - 1]
        return total
