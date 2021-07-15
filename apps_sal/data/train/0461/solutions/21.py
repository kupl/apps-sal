class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        def dfs(employee, time):
            self.result = max(self.result, time)
            for sub in subordinates[employee]:
                dfs(sub, time + informTime[employee])
            
        subordinates = collections.defaultdict(list)
        self.result = 0
        for i, m in enumerate(manager):
            if i != headID:
                subordinates[m].append(i)
        dfs(headID, 0)
        return self.result
            
        
    # def dfs(self, id):
    #     return max(informTime[id] + self.dfs(sub) for sub in subordinates[id]) if id in subordinates else 0

