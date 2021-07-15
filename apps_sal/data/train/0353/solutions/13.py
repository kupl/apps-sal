class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9+7
        s = sorted(nums)
        
        powers = [1]
        for _ in s: powers.append(powers[-1] * 2)
        
        j = len(s) - 1
        c = 0
        for i, n in enumerate(s):
            
            while j > i and n + s[j] > target: j -=1
            
            if i <= j and s[i] + s[j] <= target:
                c += powers[j - i]
                # print(i, j, c)
            
        return c % MOD
