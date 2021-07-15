class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find(x):
            if x != par[x]:
                par[x] = find(par[x])
            return par[x]
        def union(x, y):
            x, y = list(map(find, [x, y]))
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                par[y] = x
                rank[x] += rank[x] == rank[y]
                return True
            else:
                return False
            
        indegree = [0] * n
        cnt = n
        par = list(range(n))
        rank = [0] * n
        for parent, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l != -1:
                indegree[l] += 1
                if union(parent, l):
                    cnt -= 1
            if r != -1:
                indegree[r] += 1
            
                if union(parent, r):
                    cnt -= 1
        return sum(indegree) == n - 1 and cnt == 1

