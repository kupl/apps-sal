class Solution:

    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        tup = []
        dic = {}
        for i in range(0, len(profit)):
            tup.append((profit[i], difficulty[i]))
        worker.sort(reverse=True)
        tup.sort(reverse=True)
        indx = 0
        t_indx = 0
        res = 0
        while indx < len(worker):
            while t_indx < len(profit) and worker[indx] < tup[t_indx][1]:
                t_indx += 1
            if t_indx < len(profit):
                res += tup[t_indx][0]
            indx += 1
        return res
