class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        combined = sorted(zip(difficulty,profit))
        worker.sort()
        n = len(worker)
        start = 0
        net_profit = 0
        current_profit = 0
        for i in range(n):
            while start< len(difficulty) and combined[start][0]<=worker[i]:
                current_profit = max(combined[start][1],current_profit)
                start += 1
            net_profit += current_profit
        return net_profit
