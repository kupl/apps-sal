class Solution:

    def numTeams(self, rating: List[int]) -> int:
        p = 0
        res = 0
        while p < len(rating):
            less = sum([1 for i in range(p) if rating[i] < rating[p]])
            more = sum([1 for i in range(p + 1, len(rating)) if rating[i] > rating[p]])
            more1 = sum([1 for i in range(p) if rating[i] > rating[p]])
            less1 = sum([1 for i in range(p + 1, len(rating)) if rating[i] < rating[p]])
            res += less * more + more1 * less1
            p += 1
        return res
