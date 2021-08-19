class TreeNode:

    def __init__(self, val):
        self.val = val
        self.children = []


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = []
        for (idx, _) in enumerate(manager):
            nodes.append(TreeNode(informTime[idx]))
        for (idx, m) in enumerate(manager):
            if idx != headID:
                nodes[m].children.append(nodes[idx])
        root = nodes[headID]
        path_sum = 0
        max_path_sum = 0

        def dfs(node):
            nonlocal path_sum
            nonlocal max_path_sum
            if not node.children:
                max_path_sum = max(max_path_sum, path_sum + node.val)
                return
            for child in node.children:
                path_sum += node.val
                dfs(child)
                path_sum -= node.val
        dfs(root)
        return max_path_sum
