class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        
        if n < 3:
            return 0
        
        results = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range (j + 1, n):
                    if rating[i] < rating[j] and rating[j] < rating[k]:
                        results += 1
                    elif rating[i] > rating[j] and rating[j] > rating[k]:
                        results +=1
        return results
