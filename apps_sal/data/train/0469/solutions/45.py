class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        visited = set()
        for i in range(n):
            if leftChild[i] != -1:
                visited.add(leftChild[i])
            if rightChild[i] != -1:
                visited.add(rightChild[i])
        queue = list(set(list(range(n))) - visited)
        if len(queue) != 1:
            return False
        visited = set()
        while queue:
            curr = queue.copy()
            queue = []
            for c in curr:
                if c in visited:
                    return False
                visited.add(c)
                if leftChild[c] != -1:
                    queue.append(leftChild[c])
                if rightChild[c] != -1:
                    queue.append(rightChild[c])
        return len(visited) == n
