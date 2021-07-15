class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3: 
            return 0
        
        ans = 0
        
        for i in range(0, len(rating)-2):
            for j in range(i + 1, len(rating) - 1):
                for k in range(j + 1, len(rating)):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        ans += 1
                    elif rating[i] > rating[j] and rating[j] > rating[k]:
                        ans += 1 
        return ans

