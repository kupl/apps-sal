class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                if(rating[i] == rating[j]):
                    continue
                for k in range(j+1,n):
                    if(rating[i] == rating[k] or rating[j] == rating[k]):
                        continue
                    if(rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]):
                        teams += 1
        
        return teams
