class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10 ** 9 + 7
        dp =collections.deque([[1] * 7 for i in range(max(rollMax) + 1)])
        dp[-1][-1] = 6
        for i in range(2,  n + 1):
            dp2 = [0] * 7
            for j in range(6):
                if i - rollMax[j] <= 0:
                    dp2[j] = dp[-1][-1]
                elif i - rollMax[j] == 1:
                    dp2[j] = dp[-1][-1] - 1 
                else:
                    p = dp[-rollMax[j] - 1]
                    dp2[j] = (dp[-1][-1] - p[-1] + p[j]) % MOD
                dp2[-1] = (dp2[-1] + dp2[j]) % MOD
            dp.popleft()
            dp.append(dp2)
        return dp[-1][-1]

