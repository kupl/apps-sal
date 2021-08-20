class Solution:

    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        parents = [-1] * n
        for p in range(n):
            if leftChild[p] != -1:
                if parents[leftChild[p]] != -1:
                    return False
                parents[leftChild[p]] = p
            if rightChild[p] != -1:
                if parents[rightChild[p]] != -1:
                    return False
                parents[rightChild[p]] = p
        found = False
        for p in parents:
            if p == -1:
                if found:
                    return False
                found = True
        visit = [0] * n

        def dfs(ix):
            if ix == -1:
                return True
            if visit[ix] == 1:
                return False
            visit[ix] = 1
            if not dfs(parents[ix]):
                return False
            visit[ix] = 2
            return True
        for i in range(n):
            if visit[i] == 2:
                continue
            if not dfs(i):
                return False
        return True
