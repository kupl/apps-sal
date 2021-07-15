class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def union(origin, destination, parents, rank):
            parent_origin = find(origin, parents)
            parent_destination = find(destination, parents)
            if parent_origin == parent_destination:
                return False
            if rank[parent_origin] < rank[parent_destination]:
                parents[parent_origin] = parents[parent_destination]
            else:
                parents[parent_destination] = parents[parent_origin]
                if rank[parent_origin] == rank[parent_destination]:
                    rank[parent_origin] += 1
            return True

        def find(x, parents):
            if parents[x] == x:
                return parents[x]
            return find(parents[x], parents)

        parents = [n for n in range(n)]
        rank = [0 for _ in range(n)]
        for i, (left, right) in enumerate(zip(leftChild, rightChild)):
            if left != -1:
                if not union(i, left, parents, rank):
                    return False
            if right != -1:
                if not union(i, right, parents, rank):
                    return False
        return len({find(x, parents) for x in range(n)}) == 1
