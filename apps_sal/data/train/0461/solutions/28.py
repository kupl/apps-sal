class Solution:

    def numOfMinutes(self, n: int, head_id: int, manager: List[int], inform_time: List[int]) -> int:
        children = [[] for _ in range(n)]
        for (id, man_id) in enumerate(manager):
            if man_id >= 0:
                children[man_id].append(id)

        def dfs(id):
            t = inform_time[id]
            if children[id]:
                t += max((dfs(ch) for ch in children[id]))
            return t
        return dfs(head_id)
