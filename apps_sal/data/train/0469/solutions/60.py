class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        ingress = [0] * n
        g = defaultdict(list)
        
        # construct a graph and ingress 
        for i in range(n):
            if leftChild[i] != -1:
                ingress[leftChild[i]] += 1
                g[i].append(leftChild[i])
            
            if rightChild[i] != -1:
                ingress[rightChild[i]] += 1
                g[i].append(rightChild[i])
            
        # check only one root or two ingress
        if ingress.count(0) > 1 or max(ingress) > 1:
            return False
        
        # check any cycle
        def dfs(node):
            
            visited.add(node)
            visiting.add(node)
            
            for neigh in g[node]:
                
                if neigh not in visited and dfs(neigh):
                    return True
                elif neigh in visiting:
                    return True
            
            visiting.remove(node)
            return False
        
        visited = set() 
        visiting = set() 
        
        for i in range(n):
            if i not in visited:
                if dfs(i):
                    return False # cycle detected
                
        return True
