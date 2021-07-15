class Solution:
    def numTeams(self, rating: List[int]) -> int: 
        
        # can use DP to speed up 
        
        # iteraton methods
        res = 0
        for com in combinations(rating, 3): 
            if com[0] > com[1] > com[2] or com[0] < com[1] < com[2]: 
                res += 1 
                
        return res
