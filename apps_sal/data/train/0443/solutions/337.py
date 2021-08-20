class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0
        l = len(rating)
        for i in range(0, l - 2):
            right = [x for x in rating[i + 1:] if x > rating[i]]
            res += sum([len([x for x in right[i + 1:] if x > right[i]]) for i in range(len(right))])
            right = [x for x in rating[i + 1:] if x < rating[i]]
            res += sum([len([x for x in right[i + 1:] if x < right[i]]) for i in range(len(right))])
        return res
