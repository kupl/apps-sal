class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def isValid(a,b,c):
            return (a < b < c) or (a > b > c)
        
        count = 0
        for i in range(len(rating)-2):
            for j in range(i, len(rating)-1):
                for k in range(j, len(rating)):
                    if isValid(rating[i], rating[j], rating[k]):
                        count += 1
        return count
                        
                    

