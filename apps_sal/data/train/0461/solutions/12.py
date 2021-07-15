class Solution:
    def __init__(self):
        self.res = 0
        
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(set) 
        for i, m in enumerate(manager):
            graph[m].add(i)
        def helper(emp, time):
            if emp not in graph:
                self.res = max(self.res, time)
                return
            for e in graph[emp]:
                helper(e, time + informTime[emp])
        helper(headID, 0)
        return self.res
