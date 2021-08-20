class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = defaultdict(lambda: [])
        for (employee, m) in enumerate(manager):
            children[m].append(employee)

        def dfs(e, total_min):
            cur_time = total_min + informTime[e]
            if len(children[e]) == 0:
                return cur_time
            max_time = cur_time
            for employee in children[e]:
                max_time = max(max_time, dfs(employee, cur_time))
            return max_time
        return dfs(headID, 0)
