class Solution:

    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:

        def dfs(id):
            if manager[id] >= 0:
                inform_time[id] += dfs(manager[id])
                manager[id] = -1
            return inform_time[id]
        return max((dfs(id) for id in range(n)))
