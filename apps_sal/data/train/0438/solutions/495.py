class Node:

    def __init__(self, left, right):
        self.leftvalue = left
        self.rightvalue = right
        self.nextleft = None
        self.nextright = None


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        n = len(arr)
        root = Node(1, n)
        chk = False

        def dfs(u, node):
            nonlocal chk
            nonlocal m
            if chk:
                return
            if not node.nextleft and (not node.nextright):
                if u == node.leftvalue:
                    node.leftvalue += 1
                    if node.rightvalue - node.leftvalue + 1 == m:
                        chk = True
                    return
                if u == node.rightvalue:
                    node.rightvalue -= 1
                    if node.rightvalue - node.leftvalue + 1 == m:
                        chk = True
                    return
                if u - node.leftvalue == m or node.rightvalue - u == m:
                    chk = True
                    return
                node.nextleft = Node(node.leftvalue, u - 1)
                node.nextright = Node(u + 1, node.rightvalue)
                return
            if node.nextleft.leftvalue <= u <= node.nextleft.rightvalue:
                dfs(u, node.nextleft)
            elif node.nextright.leftvalue <= u <= node.nextright.rightvalue:
                dfs(u, node.nextright)
        if m == len(arr):
            return n
        ans = n
        for i in range(len(arr) - 1, -1, -1):
            dfs(arr[i], root)
            ans -= 1
            if chk:
                return ans
        return -1
