class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [idx for idx in range(n)]

        def find(idx):
            original_idx = idx
            height = 0
            while parents[idx] != idx:
                height += 1
                idx = parents[idx]
            parents[original_idx] = idx
            return idx, height

        # Returns false if the two elements are already in the same group
        def union(idx1, idx2):
            parent1, _ = find(idx1)
            parent2, _ = find(idx2)
            if parent1 == parent2:
                return False
            parents[parent1] = parent2
            return True
        # [1, 3, 3, 3]
        for idx1, idx2 in enumerate(leftChild):
            if idx2 == -1:
                continue
            if not union(idx1, idx2):
                return False

        for idx1, idx2 in enumerate(rightChild):
            if idx2 == -1:
                continue
            if not union(idx1, idx2):
                return False

        group, _ = find(0)
        for idx in range(n):
            if find(idx)[0] != group:
                return False
        return True
