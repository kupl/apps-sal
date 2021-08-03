class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        self.memo = collections.defaultdict(int)
        self.stoneValue = stoneValue
        score = self.dfs(0)
        return 'Tie' if score == 0 else 'Alice' if score > 0 else 'Bob'

    def dfs(self, start):
        if start >= len(self.stoneValue):
            return 0

        if start in self.memo:
            return self.memo[start]

        self.memo[start] = float('-inf')
        score = 0

        for i in range(start, min(len(self.stoneValue), start + 3)):
            score += self.stoneValue[i]
            self.memo[start] = max(self.memo[start], score - self.dfs(i + 1))

        return self.memo[start]
