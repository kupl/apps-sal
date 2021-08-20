class Solution:

    def numTeams(self, rating: List[int]) -> int:
        ans = 0
        for pt1 in range(len(rating) - 2):
            for pt2 in range(pt1 + 1, len(rating) - 1):
                if rating[pt1] < rating[pt2]:
                    for pt3 in range(pt2 + 1, len(rating)):
                        if rating[pt2] < rating[pt3]:
                            ans += 1
                if rating[pt1] > rating[pt2]:
                    for pt3 in range(pt2 + 1, len(rating)):
                        if rating[pt2] > rating[pt3]:
                            ans += 1
        return ans
