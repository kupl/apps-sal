class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:

        parent = {}
        for i in range(n):
            if leftChild[i] != -1:
                if leftChild[i] in parent:
                    return False
                parent[leftChild[i]] = i
            if rightChild[i] != -1:
                if rightChild[i] in parent:
                    return False
                parent[rightChild[i]] = i

        if len(parent) != n - 1:
            return False
        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)
        for x in parent:
            union(x, parent[x])
        return len(set([find(x) for x in range(n)])) == 1
