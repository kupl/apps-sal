class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combined = []

        for i in range(len(difficulty)):
            combined.append((difficulty[i], profit[i]))

        combined = sorted(combined, key=lambda x: x[0])
        total = 0
        i = 0
        best_profit = 0

        for w in sorted(worker):
            while i < len(combined) and w >= combined[i][0]:
                best_profit = max(best_profit, combined[i][1])
                i += 1

            total += best_profit

        return total
