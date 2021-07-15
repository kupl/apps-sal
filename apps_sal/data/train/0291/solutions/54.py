class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        
        # https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/discuss/758041/Python-O(1)-Space-Clear-Solution
        
        if not arr: return 0
        cum = 0
        odd, even = 0, 1
        res = 0
        MOD = 10**9+7
        for num in arr:
            cum += num
            #print(odd,even, cum)
            if cum % 2:
                res += even
                odd += 1
            else:
                res += odd
                even += 1
            #print(odd,even, res)
            #print(\"________________\")
            res %= MOD
        return res%MOD

