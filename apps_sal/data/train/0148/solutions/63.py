class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        mapProfit = dict()
        for i in range(len(difficulty)):
            if difficulty[i] in mapProfit:
                mapProfit[difficulty[i]] = max(mapProfit[difficulty[i]], profit[i])
            else:
                mapProfit[difficulty[i]] = profit[i]
        l = list()
        maxDiff = max(difficulty)
        for i in range(maxDiff + 1):
            if i in mapProfit:
                l.append(mapProfit[i])
            else:
                l.append(0)

        maxFromBegin = 0
        for i in range(len(l)):
            if l[i] < maxFromBegin:
                l[i] = maxFromBegin
            else:
                maxFromBegin = l[i]
        res = 0
        for work in worker:
            if work > maxDiff:
                res += l[-1]
            else:
                res += l[work]
        return res
