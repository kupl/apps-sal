class Solution:

    def numMin(self, total_time, n: int, headID: int, subordinates: List[int], informTime: List[int]) -> int:
        if subordinates[headID] == []:
            return total_time
        else:
            return max((self.numMin(informTime[headID] + total_time, n, e, subordinates, informTime) for e in subordinates[headID]))

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for x in range(n)]
        for (i, m) in enumerate(manager):
            if m != -1:
                subordinates[m].append(i)
        print(subordinates)
        return self.numMin(0, n, headID, subordinates, informTime)
