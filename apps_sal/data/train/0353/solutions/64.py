class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # two pointer solution
        nums.sort()
        ans = 0
        for i in range(len(nums)):
            if 2 * nums[i] > target:
                break
            hi = len(nums) - 1
            lo = i
            while lo <= hi:
                mid = (hi + lo) // 2
                if nums[i] + nums[mid] > target:
                    hi = mid - 1
                else:
                    lo = mid + 1
            print(hi)
            ans = (ans + ((1 << (hi - i)))) % (10**9 + 7)
        return ans
