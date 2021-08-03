class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty, profit = zip(*sorted(zip(difficulty, profit)))

        profit_table = {}  # maps difficulty to profit

        for i, (d, p) in enumerate(zip(difficulty, profit)):
            if i > 0:
                profit_table[d] = max(p, profit_table[difficulty[i - 1]])
            else:
                profit_table[d] = p

        value = 0

        d_index = len(difficulty) - 1
        for w in reversed(sorted(worker)):
            while d_index >= 0 and difficulty[d_index] > w:
                d_index -= 1
            if d_index >= 0:
                value += profit_table[difficulty[d_index]]
        return value
