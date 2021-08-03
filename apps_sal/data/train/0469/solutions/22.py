class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        tree = {}
        notroots = set()
        for i in range(n):
            tree[i] = []
            left = leftChild[i]
            right = rightChild[i]
            if left != -1:
                notroots.add(left)
                tree[i].append(left)
            if right != -1:
                notroots.add(right)
                tree[i].append(right)
        if len(notroots) == n:
            return False

        def helper(node):
            if node not in tree:
                path.add(node)
                return True
            if node in path:
                return False
            path.add(node)
            children = tree[node]
            nchild = len(children)
            for i in range(nchild):
                child = children[i]
                if not helper(child):
                    return False
            return True

        path = set()
        for i in range(n):
            if i not in notroots:
                if not helper(i):
                    return False
                break
        for i in range(n):
            if i not in path:
                return False
        return True
