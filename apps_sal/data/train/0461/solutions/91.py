from collections import defaultdict

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        child_list = defaultdict(list)
        for i in range(n):
            j = manager[i]
            if j >= 0:
                child_list[j].append(i)
        
        def step(eid):
            children = child_list[eid]
            if not children:
                return 0
            
            return informTime[eid] + max(step(cid) for cid in children)
        
        return step(headID)

