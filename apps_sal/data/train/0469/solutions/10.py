class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def method1():
            def dfs(node):
                if node>=n:
                    return False
                
                if node in seen:
                    return False
                
                seen.add(node)
                L=True
                if leftChild[node]!=-1:
                    L=dfs(leftChild[node])
                    
                R=True
                if rightChild[node]!=-1:
                    R=dfs(rightChild[node])
                    
                return L and R
            
            seen=set()
            valid = dfs(0)
            print(len(seen),valid)
            return valid and len(seen)==n
        
        #return method1()
    
        def method2():
            indeg=collections.defaultdict(int)
            for i in range(n):
                if leftChild[i]!=-1:
                    indeg[leftChild[i]]+=1
                if rightChild[i]!=-1:
                    indeg[rightChild[i]]+=1
                    
            root=0
            for i in range(n):
                if indeg[i]==0:
                    root=i
            
            def dfs(node):
                if node>=n:
                    return False
                
                if node in seen:
                    return False
                
                seen.add(node)
                L=True
                if leftChild[node]!=-1:
                    L=dfs(leftChild[node])
                    
                R=True
                if rightChild[node]!=-1:
                    R=dfs(rightChild[node])
                    
                return L and R
            
            seen=set()
            valid = dfs(root)
            print(len(seen),valid)
            return valid and len(seen)==n
        
        return method2()
