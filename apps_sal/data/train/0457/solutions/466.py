'''
find the minimum number of coins that you need to make up the amt -> DP

recursive
amt 
c1, c2, c3 
count = float('inf')
base case:
    if amt<0:
       return -1
    if amt == 0:
        return 0
for coin in coins:
  count = min(count,1+coinchangehelper(amt-coin))


recursion with memoization

'''


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        def coinchangehelper(rem):
            if rem < 0:
                return -1
            if rem == 0:
                return 0
            if rem in memo:
                return memo[rem]
            count = float('inf')
            for coin in coins:
                sub = coinchangehelper(rem - coin)
                if sub >= 0:
                    count = min(count, 1 + sub)
            memo[rem] = count
            return memo[rem]
        memo = {}
        res = coinchangehelper(amount)
        return res if res != float('inf') else -1
