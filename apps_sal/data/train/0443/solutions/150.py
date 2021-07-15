class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) <= 2: 
            return 0
        n = len(rating)
        cnt = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                        cnt += 1
        
        return cnt
    
    def numTeams1(self, rating: List[int]) -> int:
        pass

