class Solution:
    def validateBinaryTreeNodes(self, nodes: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        
        num_edges = 0
        graph = collections.defaultdict(list)
        indegree = {i: 0 for i in range(nodes)}
        parents = {i: None for i in range(nodes)}
        # print(parents)
        for n, (l, r) in enumerate(zip(leftChild, rightChild)):
            if l != -1:
                num_edges += 1
                graph[n].append(l)
                if parents[l] is not None or parents[n] == l:
                    return False
                parents[l] = n
                indegree[l] += 1
            if r != -1:
                num_edges += 1
                graph[n].append(r)
                if parents[r] is not None or parents[n] == r:
                    return False
                parents[r] = n
                indegree[r] += 1
                
        # There must be exactly (n - 1) edges
        if num_edges != nodes - 1:
            return False
        
        # For each node, except for the root, there must be only 1 parent
        
        # FIND ALL ROOT NODES (IE. THOSE WITHOUT PARENT) - O(N)
        roots = [i for i in range(len(parents)) if parents[i] is None]

        # CHECK IF THERE'S EXACTLY 1 ROOT NODE  - O(1)
        if len(roots) != 1:
            return False
        
        # ENSURE ROOT HAS > 1 CHILD, IF N > 1 - O(N)
        root = roots[0]
        return max(leftChild[root], rightChild[root]) != -1 or nodes == 1
        

