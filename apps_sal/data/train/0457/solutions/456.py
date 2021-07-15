class Solution:
    def recursion(self, coins, remain, dic):
        if(remain < 0):
            return float('inf')
        if(remain == 0):
            return 0
        if(remain in dic.keys()):
            return dic[remain]
        min_coin = float('inf')
        for coin in coins:
            number_coin = None
            prev_num  = self.recursion(coins, remain - coin, dic)
            if(prev_num == float('inf')):
                number_coin = prev_num
            else:
                number_coin = prev_num + 1
            min_coin = min(min_coin, number_coin)
        dic[remain] = min_coin
        return min_coin
    def coinChange(self, coins: List[int], amount: int) -> int:
        remain = amount
        count = 0
        dic = {}
        number = self.recursion(coins, remain, dic)
        if(number == float('inf')):
            return -1
        else:
            return number
