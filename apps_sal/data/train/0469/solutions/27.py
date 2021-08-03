class DSU:
    def __init__(self, n):
        self.n = n
        self.parent = [x for x in range(n)]
        self.rank = [0 for x in range(n)]

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, s, t):
        sp, tp = self.find(s), self.find(t)
        if sp == tp:
            return False
        if self.rank[sp] > self.rank[tp]:
            self.parent[tp] = sp
        elif self.rank[sp] < self.rank[tp]:
            self.parent[sp] = tp
        else:
            self.parent[sp] = tp
            self.rank[tp] += 1
        return True


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        edges = set()
        net = DSU(n)
        for idx in range(n):
            if leftChild[idx] != -1:
                leftEdge = (min(idx, leftChild[idx]), max(idx, leftChild[idx]))
                if leftEdge in edges:
                    return False
                edges.add(leftEdge)
                if not net.union(idx, leftChild[idx]):
                    return False
            if rightChild[idx] != -1:
                rightEdge = (min(idx, rightChild[idx]), max(idx, rightChild[idx]))
                if rightEdge in edges:
                    return False
                edges.add(rightEdge)
                if not net.union(idx, rightChild[idx]):
                    return False
        return len(edges) == n - 1
