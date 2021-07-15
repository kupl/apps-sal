class Solution:
    def numTeams(self, rating: List[int]) -> int:
        if len(rating) < 3:
            return 0
        
        
        teams: int = 0
        for i, s1 in enumerate(rating):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    s2 = rating[j]
                    s3 = rating[k]
                    if s1 > s2 > s3 or s1 < s2 < s3:
                        teams += 1
        
        return teams
