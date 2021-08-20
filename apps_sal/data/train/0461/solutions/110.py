class Node:

    def __init__(self, id):
        self.id = id
        self.children = []


class Solution:

    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = []
        for i in range(n):
            nodes.append(Node(i))
        rootId = -1
        for i in range(n):
            if manager[i] != -1:
                nodes[manager[i]].children.append(nodes[i])
            else:
                rootId = i
        self.totalTime = 0

        def dfs(root, time):
            if not root:
                return
            self.totalTime = max(self.totalTime, time)
            for node in root.children:
                dfs(node, time + informTime[root.id])
        dfs(nodes[rootId], 0)
        return self.totalTime
