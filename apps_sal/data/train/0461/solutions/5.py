class Node:
    def __init__(self, val):
        self.val = val
        self.subordinates = []


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = [Node(t) for t in informTime]

        root = None
        for k, v in enumerate(manager):
            if v >= 0:
                nodes[v].subordinates.append(nodes[k])
            else:
                root = nodes[k]

        ans = 0

        def dfs(node, path):
            nonlocal ans
            if not node.subordinates:
                ans = max(ans, path + node.val)
                return
            for n in node.subordinates:
                dfs(n, n.val + path)

        dfs(root, root.val)

        return ans

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        children = [[] for i in range(n)]

        for k, v in enumerate(manager):
            if v >= 0:
                children[v].append(k)

        def dfs(i):
            return max([dfs(j) for j in children[i]] or [0]) + informTime[i]

        return dfs(headID)
