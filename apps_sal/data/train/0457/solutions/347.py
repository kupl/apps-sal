INF = 100000000000000000


def hashIntArr(i_arr):
    return '-'.join(list(map(str, i_arr)))


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        mc = [[0 if j == 0 else INF for j in range(amount + 1)] for _ in range(len(coins) + 1)]
        for c in range(1, len(coins) + 1):
            coin_value = coins[c - 1]

            for a in range(1, amount + 1):
                if coin_value <= a:
                    mc[c][a] = min(1 + mc[c][a - coin_value], mc[c - 1][a])
                else:
                    mc[c][a] = mc[c - 1][a]

        min_coins = mc[len(coins)][amount]
        return min_coins if min_coins < INF else -1
