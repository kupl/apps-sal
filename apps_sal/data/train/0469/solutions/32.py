from collections import defaultdict


class Solution:
    def DFS(self, edges, root, visited):
        for child in edges[root]:
            if child in visited:
                return False
            else:
                visited.add(child)
                if not self.DFS(edges, child, visited):
                    return False
        return True

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        master_list = leftChild + rightChild
        children = set(master_list) - set([-1])
        parent = set(range(n)) - children
        if len(parent) != 1:
            return False
        parent = list(parent)[0]

        edges = defaultdict(list)
        for i in range(n):
            if leftChild[i] != -1:
                edges[i].append(leftChild[i])

            if rightChild[i] != -1:
                edges[i].append(rightChild[i])
        visited = set()
        visited.add(parent)
        if not self.DFS(edges, parent, visited):
            return False
        return len(visited) == n
