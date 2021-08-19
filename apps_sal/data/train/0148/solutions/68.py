def createListOfProfitDiff(profit, difficulty):
    profit_diff = []
    for i in range(len(profit)):
        profit_diff.append((profit[i], difficulty[i]))
    return profit_diff


class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        w = sorted(worker)
        w.reverse()
        dp = []
        for i in range(len(profit)):
            dp.append((profit[i], difficulty[i]))
        dp.sort(key=lambda x: x[0])
        dp.reverse()
        i = 0
        count = 0
        for p in dp:
            while i < len(w) and p[1] <= w[i]:
                count += p[0]
                i += 1
        return count
