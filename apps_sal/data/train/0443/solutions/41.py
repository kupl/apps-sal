class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        l = len(rating)
        for i in range(0, l - 2):
            for j in range(i + 1, l - 1):
                res += len([x for x in rating[j+1:] if (rating[j] < x) == (rating[i] < rating[j])])

        return res
