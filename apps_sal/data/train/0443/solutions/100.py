class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        for i in range(len(rating)):
            l = [rating[i]]
            for j in range(i+1,len(rating)):
                l.append(rating[j])
                for k in range(j+1,len(rating)):
                    if (l[0] > l[1] and l[1] > rating[k]) or (l[0] < l[1] and l[1] < rating[k]):
                        count += 1
                l = l[:1]
        return count
