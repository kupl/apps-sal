class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        state = [float('inf')]*amount
        if amount <1:
            return 0
        max_coin = 0
        for c in coins:
            max_coin = max(c,max_coin)
            if c<= amount:
                state[c-1] = 1
        for i in range(amount):
            for c in coins:
                if i-c>=0:
                    state[i] = min(state[i-c]+1,state[i])
        
        return state[-1] if state[-1] != float('inf') else -1

