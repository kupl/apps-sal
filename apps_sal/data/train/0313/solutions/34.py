class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BST:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, root, v):
        if v < root.val:
            if not root.left:
                root.left = Node(v)
            else:
                self._insert(root.left, v)
        else:
            if not root.right:
                root.right = Node(v)
            else:
                self._insert(root.right, v)

    def findBounds(self, value, lower, upper):
        root = self.root
        while root:
            if root.val < value:
                lower = root.val
                root = root.right
            else:
                upper = root.val
                root = root.left

        return (lower, upper)


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        n = len(bloomDay)
        if m * k > n:
            return -1

        h = [(-d, f) for f, d in enumerate(bloomDay)]
        heapq.heapify(h)

        bst = BST()
        fit = n // k
        while True:
            day, flower = heapq.heappop(h)
            l, u = bst.findBounds(flower, -1, n)
            fit += (flower - l - 1) // k + (u - flower - 1) // k - (u - l - 1) // k
            bst.insert(flower)
            if fit < m:
                return -day
