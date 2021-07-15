class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        teams=0
        for i in range(n):
            for k in range(i+2,n):
                if rating[i]<rating[k]:
                    teams+=len([r for r in rating[i+1:k] if rating[i]<r<rating[k]])
                else:
                    teams+=len([r for r in rating[i+1:k] if rating[i]>r>rating[k]])
        
        # for i in range(n):
        #     for j in range(i+1,n):
        #         for k in range(j+1,n):
        #             if rating[i]<rating[j]<rating[k] or rating[i] > rating[j] > rating[k]:
        #                 teams+=1
        return teams

