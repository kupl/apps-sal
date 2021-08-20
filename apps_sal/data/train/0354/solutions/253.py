class Solution:

    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        memo = {}

        def helper(n, consec):
            if rollMax[consec[0]] < consec[1]:
                return 0
            elif n == 0:
                return 1
            elif (n, consec) in memo:
                return memo[n, consec]
            res = []
            for i in range(1, 7):
                if i - 1 == consec[0]:
                    res.append(helper(n - 1, (consec[0], consec[1] + 1)))
                else:
                    res.append(helper(n - 1, (i - 1, 1)))
            memo[n, consec] = sum(res) % (10 ** 9 + 7)
            return memo[n, consec]
        return helper(n, (0, 0))
