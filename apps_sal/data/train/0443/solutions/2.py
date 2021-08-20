class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            (l_small, l_great) = (0, 0)
            for j in range(i):
                if rating[i] < rating[j]:
                    l_great += 1
                elif rating[i] > rating[j]:
                    l_small += 1
            (r_small, r_great) = (0, 0)
            for k in range(i + 1, len(rating)):
                if rating[i] > rating[k]:
                    r_small += 1
                elif rating[k] > rating[i]:
                    r_great += 1
            res += l_small * r_great
            res += l_great * r_small
        return res
