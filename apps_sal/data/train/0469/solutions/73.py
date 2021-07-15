class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        uf = {}
        def find(x):
            uf.setdefault(x, x)
            if uf[x] != x: uf[x] = find(uf[x])
            return uf[x]
        def union(x, y):
            uf[find(x)] = find(y)
        
        indegree, outdegree = Counter(), Counter()
        root_cnt = 0
        
        for i, node in enumerate(leftChild):
            if node == -1: continue
            indegree[node] += 1
            outdegree[i] += 1
            union(i, node)
        for i, node in enumerate(rightChild):
            if node == -1: continue
            indegree[node] += 1
            outdegree[i] += 1
            union(i, node)
        
        for i in range(n):
            if indegree[i] == 0:
                root_cnt += 1
            elif indegree[i] != 1:
                return False
            
            if outdegree[i] > 2:
                return False
    
        return root_cnt == 1 and len(set(map(find, list(range(n)))))==1
    

