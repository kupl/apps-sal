class Solution:
    ans = 0

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Time Limit Exceeded
        d = {}
        totalTime = [-1] * n

        def help(index):
            if index == headID:
                d[index] = 0
                return 0
            else:
                m = manager[index]
                cost = 0
                if m in d:
                    cost = informTime[m] + d[m]
                else:
                    cost = informTime[m] + help(m)
                d[index] = cost
                totalTime[index] = cost
                self.ans = max(self.ans, cost)
                return cost
        for i in range(n):
            if totalTime[i] < 0:
                help(i)
        return self.ans
