from itertools import combinations
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        cnt = 0
        for c in combinations([i for i in range(len(rating))],3):
            i,j,k = c[0],c[1],c[2]
            if rating[i] < rating[j] and rating[j] < rating[k]:
                cnt +=1
            if rating[i] > rating[j] and rating[j] > rating[k]:
                cnt +=1
        return cnt
