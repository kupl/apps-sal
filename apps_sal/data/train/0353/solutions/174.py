class Solution:

    def numSubseq(self, nums: List[int], target: int) -> int:
        """
        Sort the array and grab min and max elements such that nums[min] + nums[max] <= target
        Now in the substring nums[min : max]
            min can be always selected and all combinations in [min + 1 to max] can be tried which would result in the substring having min = min and max <= max resulting in max - min <= target
        This selection yields 2^(max - min) possibilities
        """
        nums.sort()
        n = len(nums)
        res = 0
        mod = 10 ** 9 + 7
        (i, j) = (0, n - 1)
        for i in range(n):
            while i <= j and nums[i] + nums[j] > target:
                print((nums[i], nums[j]))
                j -= 1
            if i <= j and nums[i] + nums[j] <= target:
                res += pow(2, j - i)
                res %= mod
                print((nums[i], i, nums[j], j, res))
        return res
