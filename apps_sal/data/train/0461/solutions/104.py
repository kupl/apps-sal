from collections import defaultdict, deque


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def dfs(mngr):
            if not manager_map[mngr]:
                return 0
            result = 0
            result += max((inform_time + dfs(subordinate) for (subordinate, inform_time) in manager_map[mngr]))
            return result
        manager_map = defaultdict(list)
        i = 0
        for (manager_ix, time) in zip(manager, informTime):
            manager_map[manager_ix].append((i, informTime[i]))
            i += 1
        return dfs(-1)
