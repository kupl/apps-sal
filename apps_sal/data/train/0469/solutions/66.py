class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # find root and do dfs
        # look for cycle or things not visited from the root
        visited = [False] * n
        cycle = False
        
        def dfs(root):
            nonlocal cycle
            #print(root, visited, cycle)
            if root == -1:
                return
            
            if not visited[root]:
                visited[root] = True
                dfs(leftChild[root])
                dfs(rightChild[root])
            else:
                print('cycle')
                cycle = True
                
            
                   
        def find_root():
            in_degree = {}
            
            for i in range(n):
                in_degree[i] = 0
            # add -1 so u wont skip it
            in_degree[-1] = 0    
            for i in range(n):
                in_degree[leftChild[i]] += 1
                in_degree[rightChild[i]] += 1
                
            for k,v in list(in_degree.items()):
                if v == 0:
                    return k
                
        root = find_root()
        print(root)
        if root == None:
            return False
        dfs(root)
        print(cycle)
        if cycle:
            print('cycle')
            return False
        
        print(visited)
        return all(visited)
        
        
                
            
            
        


