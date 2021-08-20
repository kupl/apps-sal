from collections import defaultdict


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:

        def group_by_manager(l):
            d = defaultdict(lambda: [])
            for (ind, manager) in l:
                d[manager].append(ind)
            return d
        manager_to_subs = group_by_manager(enumerate(manager))

        def get_children(m):
            return manager_to_subs.get(m, [])

        def max_path(r):
            children = get_children(r)
            return informTime[r] + (max((max_path(c) for c in children)) if children else 0)
        return max_path(headID)
