class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        indegree = [0 for _ in range(n)]
        roots = set(range(n))
        children = set()
        for left, right in zip(leftChild, rightChild):
            if left != -1:
                indegree[left] += 1
                if left in roots:
                    roots.remove(left)
                    children.add(left)
                if indegree[left] > 1:
                    return False
            if right != -1:
                indegree[right] += 1
                if right in roots:
                    roots.remove(right)
                    children.add(right)
                if indegree[right] > 1:
                    return False

        if len(roots) != 1:
            return False

        while roots:
            new_root = next(iter(roots))
            roots.remove(new_root)
            if leftChild[new_root] != -1:
                children.remove(leftChild[new_root])
                roots.add(leftChild[new_root])
            if rightChild[new_root] != -1:
                children.remove(rightChild[new_root])
                roots.add(rightChild[new_root])

        return not children
