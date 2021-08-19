from functools import lru_cache


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # alex's best score must be greater than total score // 2
        totalScore = sum(piles)
        memo = {}

        @lru_cache(None)
        def helper(first=0, last=len(piles) - 1, ):
            if first > last:
                return 0
            isAlex = (last - first - len(piles)) % 2
            # total score from this state of the game minus ( - ) min of my opponent's score
            if isAlex:
                return max(piles[first] + helper(first + 1, last), piles[last] + helper(first, last - 1))
            else:
                return min(-piles[first] + helper(first + 1, last), -piles[last] + helper(first, last - 1))
            # memo[qstring] = myMaxScore
            # return myMaxScore

        return helper() > 0
