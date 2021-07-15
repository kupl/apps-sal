class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = len(nums)
        left = 0
        right = l -1
        ans = 0
        while left <= right:
            curr = nums[left]
            leftover = target - curr
            if leftover < curr:
                return ans % (10 ** 9 + 7 )
            ans += 1
            while nums[right] > leftover:
                right -= 1
            ans += 2 ** (right - left) - 1
            left += 1
        return ans % (10 ** 9 + 7)
            
            

