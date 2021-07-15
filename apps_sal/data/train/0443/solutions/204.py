class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        l = len(rating)
        count = 0
        
        for i in range(l - 2):
            for j in range(i + 1, l-1):
                for k in range(j + 1, l):
                    if rating[k] > rating[j] > rating[i] or rating[k] < rating[j] < rating[i]:
                        count += 1
                        
        return count
