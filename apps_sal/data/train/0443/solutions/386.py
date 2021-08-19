class Solution:

    def numTeams(self, ratings: List[int]) -> int:
        ans = 0
        for i in range(len(ratings) - 2):
            for j in range(i, len(ratings) - 1):
                if ratings[j] > ratings[i]:
                    for k in range(j, len(ratings)):
                        if ratings[k] > ratings[j]:
                            ans += 1
                if ratings[j] < ratings[i]:
                    for k in range(j, len(ratings)):
                        if ratings[k] < ratings[j]:
                            ans += 1
        return ans
