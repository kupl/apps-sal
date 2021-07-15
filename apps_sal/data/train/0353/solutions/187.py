class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        i, j, res, N = 0, len(nums) - 1, 0, 10 ** 9 + 7
        nums.sort()
        
        while i <= j:
            if nums[i] + nums[j] > target: j -= 1
            else:
                res += (2 ** (j - i)) % N
                i += 1
        return res % N

