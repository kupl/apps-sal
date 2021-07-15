class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        dic = {}
        i = 0
        j = 0
        MAX = 1
        
        if tree == None or len(tree) == 0:
            return None
        
        while j < len(tree):
            if len(dic) <= 2:
                dic[tree[j]] = j
                j+=1
            if len(dic) > 2:
                mins = len(tree) -1
                
                for val in list(dic.values()):
                    mins = min(mins,val)
                
                i = mins + 1
                del dic[tree[mins]]
            
            MAX = max(MAX,j-i)
        return MAX
            
                              
                

