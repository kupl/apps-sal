class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def cycle(node):
            if seen[node] == 1:
                return True
            if seen[node] == 2:
                return False
            seen[node] = 1
            for nei in g[node]:
                if cycle(nei):
                    return True
            seen[node] = 2
            return False
        
        indeg = [0]*n
        g = [[] for _ in range(n)]
        
        for i, (u, v) in enumerate(zip(leftChild, rightChild)):
            if u > -1:
                g[i].append(u)
                indeg[u] += 1
            if v > -1:
                g[i].append(v)
                indeg[v] += 1
                
        counts = Counter(indeg)
        # multiple roots or no root
        if counts[0] > 1 or counts[0] == 0:
            return False
        # multiple indegrees
        if any(count > 1 for count in list(counts.keys())):
            return False
        
        root = indeg.index(0)
        seen = [0]*n
        # no cycles and dfs hits all nodes (one CC)
        return not cycle(root) and all(seen[node] == 2 for node in range(n))
            

