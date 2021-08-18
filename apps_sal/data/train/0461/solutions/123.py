class Solution:
    class Node:
        def __init__(self, val, inform=0):
            self.val = val
            self.inform = inform
            self.children = []

    def traversal(self, root, time) -> int:
        if not root or root is None:
            return time
        final_time = time
        for node in root.children:
            final_time = max(final_time, self.traversal(node, time + root.inform))
        return final_time

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = {}
        root = self.Node(headID)
        d[headID] = root

        for i in range(n):
            if i == headID:
                d[headID].inform = informTime[i]
                continue
            d[i] = self.Node(i, informTime[i])

        for i, m in enumerate(manager):
            if m == -1:
                continue
            d[m].children.append(d[i])

        final_time = self.traversal(root, 0)
        return final_time
