class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        # returns the maximum points Alex can get
        mem = {}

        def dp(l, r):
            if l > r:
                return 0
            if (l, r) in mem:
                return mem[(l, r)]
            alex_turn = ((r - l) % 2 == 1)
            reward_left = dp(l + 1, r)
            reward_right = dp(l, r - 1)
            if alex_turn:
                res = max(reward_left + piles[l], reward_right + piles[r])
            else:
                res = min(reward_left, reward_right)
            mem[(l, r)] = res
            return res

        reward = dp(0, len(piles) - 1)
        total = sum(piles)
        return reward > total / 2
