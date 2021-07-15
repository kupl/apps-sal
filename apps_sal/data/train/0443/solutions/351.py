class Solution:
    def numTeams(self, rating: List[int]) -> int:
        teams = 0
        a = 0
        
        while a < len(rating) - 2:
            b = a+1
            while b < len(rating) - 1:
                c = b+1
                if rating[a] < rating[b]:
                    for c in range(c, len(rating)):
                        if rating[b] < rating[c]:
                            teams+=1
                if rating[a] > rating[b]:
                    for c in range(c, len(rating)):
                        if rating[b] > rating[c]:
                            teams+=1
                b+=1
            a+=1
            
        return teams
