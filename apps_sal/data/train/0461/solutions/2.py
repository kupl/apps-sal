class Solution:

    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        cache = [None] * n

        def dfs(id):
            if cache[id]:
                return cache[id]
            t = inform_time[id]
            if manager[id] >= 0:
                t += dfs(manager[id])
            cache[id] = t
            return t
        return max((dfs(id) for id in range(n)))
