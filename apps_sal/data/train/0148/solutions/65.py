class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        max_diff = max(difficulty)
        max_profits = [0] * (max_diff + 1)

        for diff, profit in zip(difficulty, profit):
            max_profits[diff] = max(max_profits[diff], profit)

        for i in range(1, max_diff + 1):
            max_profits[i] = max(max_profits[i], max_profits[i - 1])

        pft = 0
        for wskill in worker:
            pft += max_profits[max_diff if wskill > max_diff else wskill]

        return pft
