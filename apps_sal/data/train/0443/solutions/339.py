class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            for j in range(len(rating)):
                #Never need to check last 2
                #check for 3rd value
                if j <= i:
                    continue
                if rating[i] > rating[j]:
                    for k in rating[j:]:
                        if rating[j] > k:
                            count += 1
                elif rating[i] < rating[j]:
                    for k in rating[j:]:
                        if rating[j] < k:
                            count += 1
                           
        return count
                        

