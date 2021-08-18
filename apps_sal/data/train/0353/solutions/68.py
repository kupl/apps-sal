class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        ans, left, right = 0, 0, len(nums) - 1
        while right >= 0 and nums[right] + nums[left] > target:
            right -= 1

        while right >= 0:
            complement = target - nums[right]
            if nums[right] <= complement:
                ans += (1 << (right + 1)) - 1
                break
            else:
                while nums[left] <= complement:
                    left += 1

                if left == right:
                    ans += (1 << (right + 1)) - 2
                    break
                else:
                    ans += ((1 << left) - 1) * (1 << (right - left))
            right -= 1

        return ans % (10 ** 9 + 7)
