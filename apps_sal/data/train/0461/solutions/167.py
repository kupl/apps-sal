class Solution:
    def numMin(self, n: int, headID: int, subordinates: List[int], informTime: List[int]) -> int:
        if subordinates[headID] == []:
            return 0
        else:
            return informTime[headID] + max(self.numMin(n, e, subordinates, informTime) for e in subordinates[headID])

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates = [[] for x in range(n)]
        for i, m in enumerate(manager):
            if m != -1:
                subordinates[m].append(i)
        print(subordinates)
        return self.numMin(n, headID, subordinates, informTime)
