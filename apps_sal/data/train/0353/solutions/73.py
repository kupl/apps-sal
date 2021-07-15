class Solution:
    MOD = 10**9 + 7

    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        
        count = 0
        i, j = 0, n - 1
        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
                
                continue

            len_ = j - i + 1
            count += 2**(len_ - 1)
                
            i += 1
                    
        return count % self.__class__.MOD

