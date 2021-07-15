class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # Brute force O(n**3)
        res = 0
        for i in range(len(rating) - 2):
            for j in range(i+1,len(rating) - 1):
                if rating[j] < rating[i]:
                    # Check for increasing
                    for k in range(j+1,len(rating)):
                        if rating[k] < rating[j]:
                            res += 1
                else:
                    for k in range(j+1,len(rating)):
                        if rating[k] > rating[j]:
                            res += 1
        return res
