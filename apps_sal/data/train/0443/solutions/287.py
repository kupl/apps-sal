class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def loop(prev, remains, i):
            res = 0
            if i >= len(rating):
                return res
            if rating[i] > prev:
                if remains == 1:
                    res += 1
                else:
                    res += loop(rating[i], remains - 1, i + 1)
            res += loop(prev, remains, i + 1)
            return res
        res = 0
        res += loop(-1, 3, 0)
        rating.reverse()
        res += loop(-1, 3, 0)
        return res
