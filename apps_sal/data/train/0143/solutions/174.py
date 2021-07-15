class Solution:
    
    def totalFruit(self, tree: List[int]) -> int:
        
        blocks = [(k, len(list(v))) for k, v in itertools.groupby(tree)]
        
        ans = i = 0
        
        while i < len(blocks):
            
            types, weight = set(), 0
            
            for j in range(i, len(blocks)):
                
                types.add(blocks[j][0])
                
                weight += blocks[j][1]
                
                if len(types) >= 3:
                    
                    i = j - 1
                    
                    break
                    
                ans = max(ans, weight)
                
                
            else:
                
                break
                
        return ans
            
            
        
            
            

