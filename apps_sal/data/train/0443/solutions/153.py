class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # brute force attempt
        n = len(rating)
        ans = 0
        
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        ans += 1
                    
                    if rating[i] > rating[j] and rating[j] > rating[k]:
                        ans += 1
        return ans
