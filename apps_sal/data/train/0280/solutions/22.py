from functools import lru_cache
class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        if n == k:
            return 0
        # a string of length n, the largest cost to make it  palindrome is n // 2
        @lru_cache(None)
        def cnt(left,right): # cost to make palindrome
            if left  >= right:
                return 0
            return cnt(left+1,right-1) + (s[left] != s[right])
        
        @lru_cache(None)
        def dp(length,partition):
            if partition == length:
                return 0
            if partition == 1:
                return cnt(0,length-1)
            res = float('inf')
            for prelength in range(partition - 1,length):
                res = min(res,dp(prelength,partition-1)+cnt(prelength,length-1))
            return res
    
        return dp(n,k)

