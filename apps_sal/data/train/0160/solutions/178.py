class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        memory = [[0 for _ in range(len(piles))] for _ in range(len(piles))]
        return self.dfs(piles, 0, len(piles) - 1, True, memory) > 0

    def dfs(self, piles, start, end, turn, memory):
        if start > end:
            return 0
        if memory[start][end] != 0:
            return memory[start][end]
        if turn:
            memory[start][end] = max(piles[start] + self.dfs(piles, start + 1, end, not turn, memory), piles[end] + self.dfs(piles, start, end - 1, not turn, memory))
        else:
            memory[start][end] = min(-piles[start] + self.dfs(piles, start + 1, end, not turn, memory), -piles[end] + self.dfs(piles, start, end - 1, not turn, memory))
        return memory[start][end]
