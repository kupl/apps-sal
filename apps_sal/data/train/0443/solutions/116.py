class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # just use i,j,k three pointers. then it is O^3
        # brute-force O^3 solution would be to use three index pointers
        # spacewise, this would be just O(1)
        
        count = 0
        
        for i in range(0, len(rating)-2):
            for j in range(i+1, len(rating)-1):
                for k in range(j+1, len(rating)):
                    if ((rating[i] < rating[j]) and (rating[j] < rating[k])) or ((rating[i] > rating[j]) and (rating[j] > rating[k])):
                        count += 1
                    
        return count
        

