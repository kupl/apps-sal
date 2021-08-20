class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0
        i = 0
        j = 1
        k = 2
        while i < len(rating) - 2:
            if rating[i] < rating[j] < rating[k] or rating[i] > rating[j] > rating[k]:
                res += 1
            k += 1
            if k > len(rating) - 1:
                j += 1
                k = j + 1
            if j > len(rating) - 2:
                i += 1
                j = i + 1
                k = i + 2
        return res
