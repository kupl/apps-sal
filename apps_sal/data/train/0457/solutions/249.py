class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cal=[float('inf') for i in range(amount+1)]
        for i in range(0,amount+1):
            for j in range(len(coins)):
                if i==0:
                    cal[i]=0
                elif coins[j]<=i:
                    cal[i]=min(1+cal[i-coins[j]],cal[i])
        print(cal)
        if cal[amount] == float('inf'):
            return -1
        else:
            return cal[amount]

