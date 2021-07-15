class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ws = sorted(worker, reverse=True)
        dp = sorted(zip(difficulty, profit), key=lambda x: x[1], reverse=True)
        # print(list(dp))
        
        i = 0
        total = 0
        for w in ws:
            while dp[i][0] > w:
                i = i + 1
                if i >= len(dp):
                    return total
            total = total + dp[i][1]
        return total
