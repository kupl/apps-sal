class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:

        n = max(worker)
        s = [0 for i in range(n)]

        for i in range(len(difficulty)):
            if difficulty[i] <= n:
                s[difficulty[i] - 1] = max(s[difficulty[i] - 1], profit[i])

        for i in range(1, n):
            if s[i] < s[i - 1]:
                s[i] = s[i - 1]
        ans = sum([s[worker[i] - 1] for i in range(len(worker))])
        return ans
