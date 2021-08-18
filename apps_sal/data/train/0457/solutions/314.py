class Solution:

    def coinChangeDynamic(self, coins: List[int], amount: int, memory_dict: dict) -> int:
        if(amount < 0):
            return -1
        elif amount == 0:
            return 0
        else:
            if(memory_dict.get(amount) is None):
                recursive_call_output = []
                for coin_val in coins:
                    recursive_call_output.append(self.coinChangeDynamic(coins, amount - coin_val, memory_dict))
                min_num_coins = float('inf')
                for num_coins in recursive_call_output:
                    if num_coins >= 0 and num_coins < min_num_coins:
                        min_num_coins = num_coins

                if(min_num_coins == float('inf')):
                    memory_dict[amount] = -1
                    return -1
                else:
                    memory_dict[amount] = min_num_coins + 1
                    return min_num_coins + 1
            else:
                return memory_dict[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        return self.coinChangeDynamic(coins, amount, {})
