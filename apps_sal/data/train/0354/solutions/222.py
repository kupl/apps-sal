class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        mode = 10 ** 9 + 7
        memo = {}

        def dfs(prev, s, n):
            if n == 0:
                return 1
            if (prev, s, n) in memo:
                return memo[prev, s, n]
            else:
                res = 0
                for i in range(6):
                    if i == prev:
                        if s + 1 > rollMax[i]:
                            continue
                        else:
                            res += dfs(i, s + 1, n - 1)
                    else:
                        res += dfs(i, 1, n - 1)
                memo[prev, s, n] = res
            return res
        return dfs(0, 0, n) % mode
