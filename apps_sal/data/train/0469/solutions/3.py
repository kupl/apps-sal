class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [(idx, 0) for idx in range(n)]

        def find(idx):
            original_idx = idx
            height = 0
            while parents[idx][0] != idx:
                height += 1
                idx = parents[idx][0]
            parents[original_idx] = (idx, 0)
            return parents[idx]

        def union(idx1, idx2):
            (parent1, rank1) = find(idx1)
            (parent2, rank2) = find(idx2)
            if parent1 == parent2:
                return False
            if rank1 > rank2:
                parents[parent2] = (parent1, rank1)
            elif rank2 > rank1:
                parents[parent1] = (parent2, rank2)
            else:
                parents[parent1] = (parent2, rank2 + 1)
            return True
        for (idx1, idx2) in enumerate(leftChild):
            if idx2 == -1:
                continue
            if not union(idx1, idx2):
                return False
        for (idx1, idx2) in enumerate(rightChild):
            if idx2 == -1:
                continue
            if not union(idx1, idx2):
                return False
        (group, _) = find(0)
        for idx in range(n):
            if find(idx)[0] != group:
                return False
        return True
