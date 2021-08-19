class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        for i in range(len(profit)):
            difficulty[i] = [difficulty[i], profit[i]]
        difficulty.sort()
        for i in range(1, len(profit)):
            difficulty[i][1] = max(difficulty[i - 1][1], difficulty[i][1])

        def search(d):
            if d < difficulty[0][0]:
                return -1
            l = 0
            r = len(profit) - 1
            while l < r:
                m = (l + r + 1) // 2
                if difficulty[m][0] <= d:
                    l = m
                else:
                    r = m - 1
            return l
        res = 0
        for w in worker:
            i = search(w)
            if i >= 0:
                res += difficulty[i][1]
        return res
