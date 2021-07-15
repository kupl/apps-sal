class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) == 0:
            return 0
        types = {}
        numFruits = 0
        maxNumFruits = 0
        left = 0
        right = 0
        while(right < len(tree)):
            if tree[right] in types:
                types[tree[right]] += 1
            else:
                types[tree[right]] = 1
            numFruits += 1
            right += 1
            
            while len(types) > 2:
                if types[tree[left]] == 1:
                    del(types[tree[left]])
                else:
                    types[tree[left]] -= 1
                left += 1
                numFruits -= 1
            maxNumFruits = max(maxNumFruits, numFruits)
            
            
        return maxNumFruits
                    
                
            

            
                
                

