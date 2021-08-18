class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        for i in range(len(difficulty)):
            difficulty[i] = (difficulty[i], profit[i])
        difficulty.sort(key=lambda x: x[0])
        i, L = 0, len(difficulty)
        ans, most = 0, 0
        for wker in sorted(worker):
            while i < L and difficulty[i][0] <= wker:
                most = max(most, difficulty[i][1])
                i += 1
            ans += most
        return ans
