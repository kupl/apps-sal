class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        states = [0] * (amount + 1)
        for s in range(0, amount + 1):
            if s == 0:
                states[s] = 0
            else:
                min_c = 1e9
                for c in coins:
                    if c <= s and states[s - c] != -1:
                        min_c = min(min_c, 1 + states[s - c])
                if min_c == 1e9:
                    states[s] = -1
                else:
                    states[s] = min_c
                print(s, states[s])
        return states[amount]
