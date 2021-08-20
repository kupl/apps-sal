class Solution:

    def numTeams(self, rating: List[int]) -> int:
        res = 0
        lenn = len(rating)
        for mid in range(1, lenn - 1):
            (left_less, right_more) = (0, 0)
            (left_more, right_less) = (0, 0)
            for j in range(mid):
                if rating[j] < rating[mid]:
                    left_less += 1
                elif rating[j] > rating[mid]:
                    left_more += 1
            for j in range(mid + 1, lenn):
                if rating[j] < rating[mid]:
                    right_less += 1
                elif rating[j] > rating[mid]:
                    right_more += 1
            res += left_less * right_more + left_more * right_less
        return res
