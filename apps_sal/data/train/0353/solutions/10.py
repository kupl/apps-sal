class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        '''
         将数组排序，找符合条件的子序列的最小值与最大值
         从每一项开始，寻找符合条件的最大值位置
            In subarray nums[i~j]:
            min = nums[i], max = nums[j]
            nums[i] + nums[j] <= target
            {nums[i], (j - i - 1 + 1 values)}
            Any subset of the right part gives a valid subsequence 
            in the original array. And There are 2^(j - i) ones.
        '''
        n = len(nums)
        nums.sort()
        p = [1] * (n + 1)
        for i in range(1, n + 1):
            p[i] = p[i - 1] << 1
        res = 0
        j = n - 1
        for i in range(j + 1):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1
            if i > j:
                continue
            res += p[j - i]
        return res % (10**9 + 7)
