class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def findRoot():
            for l, r in zip(leftChild, rightChild):
                if l != -1:
                    inDegree[l] += 1
                if r != -1:
                    inDegree[r] += 1
                
            for i, count in enumerate(inDegree):
                if count == 0:
                    return i
            
            return -1
            
        def dfs(i):
            l = leftChild[i]
            r = rightChild[i]
            
            if visited[i] or (l != -1 and visited[l]) or (r != -1 and visited[r]):
                return False
            
            visited[i] = True
            
            if l == -1 and r == -1:
                return True
            elif l == -1:
                return dfs(r)
            elif r == -1:
                return dfs(l)
            else:
                return dfs(l) and dfs(r)
            
            
        inDegree = [0 for _ in range(n)]
        visited = [False for _ in range(n)]
        
        root = findRoot()
        if root == -1:
            return False
        
        ok = dfs(root)
        if not ok:
            return False
        
        return all(visited)

