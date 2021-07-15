import sys

sys.setrecursionlimit(10**6) 

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.par = None
        self.kids = []

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        nodes = [TreeNode(informTime[emp]) for emp in range(n)]
        for emp in range(n):
            if manager[emp] != -1:
                nodes[emp].par = nodes[manager[emp]]
                nodes[manager[emp]].kids.append(nodes[emp])
        
        head = nodes[headID]
        
        def helper(node):
            return node.val + max([helper(k) for k in node.kids],default=0)
        
        return helper(head)
