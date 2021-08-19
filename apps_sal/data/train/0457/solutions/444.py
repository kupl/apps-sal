class Solution:

    def back_tracking_solution(self):

        def _is_solution(amount_left):
            if amount_left == 0:
                return True
            return False

        def _process_solution(num_coins_used, fewest_coins):
            if num_coins_used < fewest_coins[0]:
                fewest_coins[0] = num_coins_used

        def _candidate_coins_start_idx(amount_left, coins, current_coin_start_idx):
            for i in range(current_coin_start_idx, len(coins)):
                if amount_left >= coins[i]:
                    return i
            return None

        def _backtrack(amount_left, num_coins_used, current_fewest_coins, coins, current_coin_start_idx):
            if _is_solution(amount_left):
                _process_solution(num_coins_used, current_fewest_coins)
            else:
                real_coin_start_idx = _candidate_coins_start_idx(amount_left, coins, current_coin_start_idx)
                if real_coin_start_idx is not None:
                    for i in range(real_coin_start_idx, len(coins)):
                        _backtrack(amount_left - coins[i], num_coins_used + 1, current_fewest_coins, coins, i)
        return _backtrack

    def dynamic_programming_solution(self):

        def _dp_bad(amount, coins):
            sorted_coins = sorted(coins)
            cache = [[float('inf')] * len(coins) for i in range(amount + 1)]
            for denom_idx in range(len(sorted_coins)):
                cache[0][denom_idx] = 0
            for amt in range(amount + 1):
                cache[amt][0] = amt // sorted_coins[0] if amt % sorted_coins[0] == 0 else float('inf')
            for i in range(1, len(cache)):
                for j in range(1, len(sorted_coins)):
                    max_num_of_denom = i // sorted_coins[j] + 1
                    for k in range(max_num_of_denom):
                        cache[i][j] = min(cache[i][j], k + cache[i - k * sorted_coins[j]][j - 1])
            return cache[amount][-1]

        def _dp_cache_recursive(amount, coins, cache):
            if amount in cache:
                return cache[amount]
            for c in coins:
                if amount >= c:
                    intermediate = 1 + _dp_cache_recursive(amount - c, coins, cache)
                    if amount in cache:
                        cache[amount] = min(cache[amount], intermediate)
                    else:
                        cache[amount] = intermediate
            return cache[amount] if amount in cache else float('inf')

        def _dp_bottom_up_1(amount, coins):
            sorted_coins = sorted(coins)
            cache = [[float('inf')] * len(coins) for i in range(amount + 1)]
            for denom_idx in range(len(sorted_coins)):
                cache[0][denom_idx] = 0
            for amt in range(1, len(cache)):
                for denom_idx in range(len(sorted_coins)):
                    amt_left = amt - sorted_coins[denom_idx]
                    if amt_left >= 0:
                        cache[amt][denom_idx] = 1 + min(cache[amt_left][0:denom_idx + 1])
            return min(cache[amount])
        return _dp_bottom_up_1

    def coinChange(self, coins: List[int], amount: int) -> int:
        result = self.dynamic_programming_solution()(amount, coins)
        return -1 if result == float('inf') else result
