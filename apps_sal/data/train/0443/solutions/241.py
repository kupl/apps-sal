class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            l = [0,0]
            g = [0,0]
            for j in range(len(rating)):
                if i!=j:
                    if rating[j] < rating[i]:
                        l[i<j]+=1
                    if rating[j] > rating[i]:
                        g[i<j]+=1
            count+= l[0]*g[1] + l[1]*g[0]
        return count

