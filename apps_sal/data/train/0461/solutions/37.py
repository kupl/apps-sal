class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjacency = collections.defaultdict(list)
        for (i, manager_id) in enumerate(manager):
            adjacency[manager_id].append(i)
        result = 0

        def traverse(worker_id, time):
            nonlocal result
            time += informTime[worker_id]
            result = max(result, time)
            list(map(lambda x: traverse(x, time), adjacency[worker_id]))
        traverse(headID, 0)
        return result
