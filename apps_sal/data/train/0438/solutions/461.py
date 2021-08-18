
class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.length = 0


class Solution:
    def findLatestStep(self, arr, m):
        def remove(node):
            left = node.left
            node.right.left = left
            left.right = node.right

        count = 0
        node = {}
        M = max(arr)
        for i in range(M + 2):
            n = Node()
            node[i] = n
            if i == 0:
                continue

            node[i - 1].right = n
            n.left = node[i - 1]

        ans = -1
        for step, i in enumerate(arr):
            node[i].length = 1
            if node[i].left.length > 0:
                node[i].length += node[i].left.length
                if node[i].left.length == m:
                    count -= 1
                remove(node[i].left)
            if node[i].right.length > 0:
                if node[i].right.length == m:
                    count -= 1
                node[i].length += node[i].right.length
                remove(node[i].right)
            if node[i].length == m:
                count += 1
            if count > 0:
                ans = step + 1
        return ans
