class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] << 1
        nums.sort()
        res = 0
        j = n - 1
        for i in range(j + 1):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i > j:
                continue
            '''
            In subarray nums[i~j]:
            min = nums[i], max = nums[j]
            nums[i] + nums[j] <= target
            {nums[i], (j - i - 1 + 1 values)}
            Any subset of the right part gives a valid subsequence 
            in the original array. And There are 2^(j - i) ones.
            '''
            res += 2**(j - i)
        return res % (10**9 + 7)
