max_cap = 7 + (10 ** 9)


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        init_seq_len = len(nums)
        nums.sort()

        l = 0
        r = init_seq_len - 1
        count = 0
        while (l <= r):
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                count += (2 ** (r - l) % max_cap)
                l += 1
        return (count % max_cap)
