class Solution:
    def numTeams(self, rating: List[int]) -> int:
        
        def helper(rating):
            
            resDict = {}
            res = 0
            for i in range(len(rating)):
                for j in range(i, len(rating)):
                    if rating[i] > rating[j]:
                        resDict[i] = resDict.get(i, 0) + 1

            for i in range(len(rating)):
                for j in range(i, len(rating)):
                    if rating[i] > rating[j]:
                        res += resDict.get(j, 0)
            return res
        return helper(rating) + helper(rating[::-1])            
        
                
                    

