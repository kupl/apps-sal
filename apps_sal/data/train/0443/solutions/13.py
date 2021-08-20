class Solution:

    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        teams = 0
        for i in range(1, n - 1):
            (lt_l, lt_r, gt_l, gt_r) = (0, 0, 0, 0)
            for j in range(n):
                if rating[i] < rating[j]:
                    if i < j:
                        gt_r += 1
                    else:
                        gt_l += 1
                elif rating[i] > rating[j]:
                    if i < j:
                        lt_r += 1
                    else:
                        lt_l += 1
            teams += lt_l * gt_r + gt_l * lt_r
        return teams
