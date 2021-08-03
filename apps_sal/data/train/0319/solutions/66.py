class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        self.cache = {}
        score = self.solve(0, stoneValue)
        return 'Alice' if score > 0 else 'Bob' if score < 0 else 'Tie'

    def solve(self, i, stoneValue):  # score diff
        n = len(stoneValue)
        if i >= n:
            return 0

        if i in self.cache:
            return self.cache[i]

        res = float('-inf')
        presum = 0

        for x in range(1, 4):
            if i + x - 1 >= n:
                break
            presum += stoneValue[i + x - 1]
            res = max(res, presum - self.solve(i + x, stoneValue))  # min-max process
        self.cache[i] = res
        return res
