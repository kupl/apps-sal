class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = []
        for i in range(len(rating)):
            for j in range(i, len(rating)):
                for k in range(j, len(rating)):
                    if(rating[i] > rating[j] and rating[j] > rating[k]):
                        res.append((rating[i], rating[j], rating[k]))
                    if(rating[i] < rating[j] and rating[j] < rating[k]):
                        res.append((rating[i], rating[j], rating[k]))
        return len(res)
