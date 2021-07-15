class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amount_list = [i for i in range(amount+1)]
        
        for i in range(amount+1):
            if i == 0:
                amount_list[i] = 0
            elif i in coins:
                amount_list[i] = 1
            else:
                temp = []
                for coin in coins:
                    if amount_list[i] - coin >= 0:
                        remainder = amount_list[i] - coin
                        min_coin = (amount_list[remainder])
                        if min_coin != -1:
                            temp.append(min_coin)
                        # print('amt: {}, coin: {}, remainder: {}, min coins {}'.format(amount_list[i], coin, remainder, min_coin))
                if len(temp) == 0:
                    amount_list[i] = -1
                else:
                    amount_list[i] = min(temp) + 1
                # print(amount_list)
                    
        return amount_list[amount]
