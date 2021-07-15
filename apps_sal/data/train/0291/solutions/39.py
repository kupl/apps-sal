class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        s = 0
        evens, odds = 0, 0
        cnt = 0
        
        for num in arr:
            s += num
            if s % 2 == 1:
                cnt += (evens+1)
                odds += 1
            else:
                cnt += odds
                evens += 1
            cnt = cnt % (10**9+7)
        return cnt
