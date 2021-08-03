class Node:
    def __init__(self, time):
        self.time = time
        self.children = []


def dfs(node):
    res = node.time
    if node.children:
        res += max(dfs(c) for c in node.children)
    return res


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = [Node(t) for t in informTime]
        for i in range(n):
            if i == headID:
                continue
            nodes[manager[i]].children.append(nodes[i])
        return dfs(nodes[headID])
