from typing import List


class TreeNode(object):
    def __init__(self, val: int):
        self.val = val
        self.children = []


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree_map = {headID: TreeNode(headID)}
        for i in range(n):
            if i == headID:
                continue
            if i not in tree_map:
                tree_map[i] = TreeNode(i)
            if manager[i] not in tree_map:
                tree_map[manager[i]] = TreeNode(manager[i])
            tree_map[manager[i]].children.append(i)

        res = 0
        root = tree_map[headID]
        queue = [(root, 0)]
        while len(queue) > 0:
            r, s = queue.pop(0)
            if len(r.children) == 0:
                res = max(res, s)
            for c in r.children:
                queue.append((tree_map[c], s + informTime[r.val]))
        return res
