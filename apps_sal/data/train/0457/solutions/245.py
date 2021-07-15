class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}

        def solve(cur):
            
            if cur in memo:
                return memo[cur]
            
            if cur == 0:
                return 0
            
            arr = [float('inf')] * len(coins)
            for i, coin in enumerate(coins):
                if cur - coin < 0:
                    arr[i] = float('inf')
                else:
                    arr[i] = solve(cur - coin) + 1
                
            ret = min(arr)
            memo[cur] = ret
            return ret
        
        ans = solve(amount)
        
        if ans == float('inf'):
            return -1
        return ans

