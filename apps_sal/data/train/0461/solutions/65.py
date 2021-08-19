class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = collections.defaultdict(list)
        for (employee, manager) in enumerate(manager):
            if employee != headID:
                tree[manager].append(employee)

        def _maxDepth(node, dist):
            if node not in tree:
                return 0
            return max((_maxDepth(child, informTime[child]) for child in tree[node])) + dist
        return _maxDepth(headID, informTime[headID])
