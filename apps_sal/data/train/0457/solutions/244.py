class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = []
        coins.sort(reverse=True)
        max_sum = 2**31-1

        def find_combinations(combination, remain, start):
            nonlocal max_sum
            if remain == 0:
                max_sum = min(max_sum, len(combination))
                return
            elif remain < 0:
                return

            for i in range(start, len(coins)):
                allowed_coins = max_sum - len(combination)
                max_value_can_be_achieved = coins[i] * allowed_coins
                if coins[i] <= remain < max_value_can_be_achieved:
                    combination.append(coins[i])
                    find_combinations(combination, remain-coins[i], i)
                    combination.pop()
                
        find_combinations([], amount, 0)
        
        if  max_sum == 2**31 -1:
            return -1
        return max_sum
        
        

