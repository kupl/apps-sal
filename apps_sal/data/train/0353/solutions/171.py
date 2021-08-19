class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()

        i, j = 0, len(nums) - 1
        res = 0

        while i <= j:
            if nums[i] + nums[j] > target:
                j -= 1
            else:
                res = (res + 2 ** (j - i)) % (10 ** 9 + 7)  # 除去左边界的元素（因为要固定它作为min），对于它右边的所有元素，都有选和不选两种可能，所以是2^N，N是右边元素数量
                i += 1

        return res
