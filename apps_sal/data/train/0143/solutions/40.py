class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        
        ans= i=0
        
        basket = {}
        
        for j, x in enumerate(tree):
            
            if x in basket:
                basket[x] += 1
            else:
                basket[x] = 1
                
            while len(basket)>=3:
                
                basket[tree[i]] -= 1
                
                if basket[tree[i]] == 0:
                    
                    del basket[tree[i]]
                
                i += 1
                
            ans = max(ans, j-i+1)
                
        return ans

