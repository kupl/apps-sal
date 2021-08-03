class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        profit = [i[1] for i in sorted(zip(difficulty, profit))]
        difficulty.sort()
        for i in range(1, len(profit)):
            profit[i] = max(profit[i], profit[i - 1])
        difficulty.append(float('inf'))
        worker.sort()
        tot = 0
        low = 0
        for w in range(len(worker)):
            low = 0
            high = len(difficulty) - 1
            while low < high:
                mid = low + (high - low) // 2
                if difficulty[mid] > worker[w]:
                    high = mid
                else:
                    low = mid + 1
            low -= 1
            if low < 0:
                low = 0
                continue
            tot += profit[low]
        return tot
