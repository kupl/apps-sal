class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort()
        coins.reverse()
        print(coins)
        change = [-1]*(amount+1)
        change[0] = 0
        for i in range(1, amount+1):
            for c1 in coins:
                #print(f'i:{i}, c1:{c1}')
                if c1 > i:
                    continue
                c2 = change[i-c1]
                if c2 >= 0:
                    if change[i] == -1:
                        change[i] = c2+1
                    else:
                        change[i] = min(c2+1, change[i])
        return change[-1]

