class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odds = 0
        evens = 1
        ans = 0
        runningsum = 0
        MOD = 10**9 + 7
        
        for a in arr:
            runningsum += a
            if runningsum%2:
                ans = (ans + evens)%MOD
                odds += 1
            else:
                ans = (ans + odds)%MOD
                evens += 1
        return ans
