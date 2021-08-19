class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:

        self.total = 0

        @lru_cache(maxsize=100000)
        #memo = [[[-1 for _ in range(n)] for _ in range(max(rollMax)+1)] for _ in range(6)]
        def digit(last, lastcount, k):
            if k == n:
                return 1
           # elif memo[last][lastcount][k] != -1:
                # return memo[last][lastcount][k]
            curnum = 0

            for i in range(6):
                if i == last and k != 0:
                    curcount = lastcount + 1
                else:
                    curcount = 1

                if rollMax[i] < curcount:
                    continue
                else:
                    curnum += digit(i, curcount, k + 1)
            #memo[last][lastcount][k] = curnum%(10**9+7)
            return curnum % (10**9 + 7)  # memo[last][lastcount][k]

        return digit(0, 0, 0)
