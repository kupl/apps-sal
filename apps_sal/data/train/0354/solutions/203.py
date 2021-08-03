class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        dp = {}

        def die(n, i, c):
            if n == 0:
                return 1
            if (n, i, c) in dp:
                return dp[(n, i, c)]
            res = 0
            for j in range(6):
                if i != j:
                    res += die(n - 1, j, 1)
                elif c < rollMax[j]:
                    res += die(n - 1, j, c + 1)
            dp[(n, i, c)] = res
            return res
        return die(n, -1, 0) % int(1e9 + 7)
