class Solution:
    def helper(self, node, sub, informTime):
        if node not in sub or len(sub[node]) == 0:
            return informTime[node]
        times = [self.helper(x, sub, informTime) for x in sub[node]]
        return max(times) + informTime[node]
    
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        sub = defaultdict(list)
        for i, m in enumerate(manager):
            sub[m].append(i)
        return self.helper(headID, sub, informTime)
