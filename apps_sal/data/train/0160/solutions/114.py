class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo = {}

        def netWin(left, right):

            if (left, right) not in memo:
                if left > right:
                    return 0

                memo[(left, right)] = -float('inf')
                memo[(left, right)] = max(memo[(left, right)], piles[left] - netWin(left + 1, right))
                memo[(left, right)] = max(memo[(left, right)], piles[right] - netWin(left, right - 1))

            return memo[(left, right)]

        res = netWin(0, len(piles) - 1)
        # print (memo, res)
        return True if res > 0 else False
