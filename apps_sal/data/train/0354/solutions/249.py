class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        return self.dieSimulator_recursive(n, rollMax)

    def dieSimulator_recursive(self, n: int, rollMax: List[int]) -> int:
        if n == 0:
            return 0

        memo = {}

        def f(n, d, r):
            if n == 1:
                return 1

            if (n, d, r) in memo:
                return memo[(n, d, r)]

            total = 0
            for nd in range(6):
                if nd != d:
                    total += f(n - 1, nd, 1)
            if r < rollMax[d]:
                total += f(n - 1, d, r + 1)

            memo[(n, d, r)] = total
            return total % (10**9 + 7)

        total = 0
        for d in range(6):
            total += f(n, d, 1)
        return total % (10**9 + 7)
