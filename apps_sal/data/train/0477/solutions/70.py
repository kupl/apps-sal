class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        memo = {}
        def dp(s):
            if s in memo:
                return memo[s]
            if s == 1:
                return '0'
            temp = dp(s-1)
            res = temp + '1' + ''.join(['0' if b == '1' else '1' for b in temp])[::-1]
            memo[s] = res
            return res
        
        return dp(n)[k-1]
