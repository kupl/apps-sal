class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.output = 0
        self.informTime = informTime
        self.dic = dic = {}
        for n, i in enumerate(manager):
            if i not in dic:
                dic[i] = []
            dic[i].append(n)

        self.helper(headID, 0)
        return self.output

    def helper(self, n, time):
        self.output = max(self.output, time)
        newtime = time + self.informTime[n]
        for i in self.dic.get(n, []):
            self.helper(i, newtime)
