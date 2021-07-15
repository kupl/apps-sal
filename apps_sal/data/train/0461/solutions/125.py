class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_sub = defaultdict(list)
        for e, m in enumerate(manager):
            manager_sub[m].append(e)
        
        res = 0
        def max_inform_time(employee, initial_time):
            subordinate_time = []
            
            for e in manager_sub[employee]:
                t = max_inform_time(e, initial_time + informTime[e])
                subordinate_time.append(t)
            
            return max(subordinate_time) if subordinate_time else initial_time

        return max_inform_time(headID, informTime[headID])
    

