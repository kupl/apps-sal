class Solution:
    def numTeams(self, rating: List[int]) -> int:

        p = 0
        res = 0
        while p < len(rating):
            left_less = sum([1 for i in range(p) if rating[i] < rating[p]])
            right_more = sum([1 for i in range(p + 1, len(rating)) if rating[i] > rating[p]])

            left_more = sum([1 for i in range(p) if rating[i] > rating[p]])
            right_less = sum([1 for i in range(p + 1, len(rating)) if rating[i] < rating[p]])

            res += left_less * right_more + left_more * right_less

            p += 1

        return res
