class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def get_inform_time(mgr):
            subords = g[mgr]
            time_to_inform = 0
            for sub in subords:
                time_to_inform = max(time_to_inform, get_inform_time(sub))
            return time_to_inform + informTime[mgr]
        g = collections.defaultdict(list)
        for (employee, mgr) in enumerate(manager):
            g[mgr].append(employee)
        return get_inform_time(headID)
