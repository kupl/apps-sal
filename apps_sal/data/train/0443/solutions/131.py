class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n=len(rating)
        c=0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if rating[i]<rating[j] and rating[j]<rating[k]:
                        c+=1
                    if rating[i]>rating[j] and rating[j]>rating[k]:
                        c+=1
        return c
