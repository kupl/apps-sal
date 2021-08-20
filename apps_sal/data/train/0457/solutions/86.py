import math


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        path_length = []
        path_length.append(0)
        for value in range(1, amount + 1):
            min_path_value = math.inf
            for coin in coins:
                path_index = value - coin
                if path_index > -1 and path_length[path_index] != -1:
                    current_min_path = path_length[path_index] + 1
                    if current_min_path < min_path_value:
                        min_path_value = current_min_path
            path_length.append(min_path_value)
        return path_length[amount] if path_length[amount] < math.inf else -1
