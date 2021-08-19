import bisect


class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        if not difficulty:
            return 0
        indices = sorted(list(range(len(difficulty))), key=lambda i: difficulty[i])
        difficulty = [difficulty[i] for i in indices]
        profit = [profit[i] for i in indices]
        max_profit = [profit[0]]
        for p in profit[1:]:
            max_profit.append(max(max_profit[-1], p))
        total = 0
        for ability in worker:
            idx = bisect.bisect_right(difficulty, ability)
            if idx > 0:
                total += max_profit[idx - 1]
        return total
