class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        people = []
        for time in informTime:
            people.append(TreeNode(time, []))
        for ID, man in enumerate(manager):
            if man != -1:
                people[man].children.append(people[ID])

        def dfs(node):
            return node.val + max(dfs(child) for child in node.children) if node.children else 0
        return dfs(people[headID])
