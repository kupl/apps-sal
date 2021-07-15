from collections import defaultdict
class Solution:
    def __init__(self):
        self.ans=0
    
    def helper(self, curr, children, timesofar):
        if not children:
            self.ans=max(self.ans, timesofar)
        for i in children:
            self.helper(i, self.graph[i], timesofar+self.informTime[i])
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.informTime=informTime
        self.graph=defaultdict(list)
        for idx,i in enumerate(manager):
            self.graph[i].append(idx)
        self.helper(headID, self.graph[headID], self.informTime[headID])
        return self.ans
