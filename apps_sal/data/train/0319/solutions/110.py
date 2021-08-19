class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.cache = {}
        score = self.solve(0, stoneValue)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'

    def solve(self, s, stoneValue):  # score diff
        n = len(stoneValue)
        if s >= n:
            return 0

        if s in self.cache:
            return self.cache[s]

        best = -2**31
        presum = 0

        for x in range(1, 4):
            if s + x - 1 >= n:
                break
            presum += stoneValue[s + x - 1]
            best = max(best, presum - self.solve(s + x, stoneValue))  # min-max process
        self.cache[s] = best
        return best
