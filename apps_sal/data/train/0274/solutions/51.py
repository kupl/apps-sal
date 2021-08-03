class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from collections import deque
        mnq = deque([])
        mxq = deque([])
        left = 0

        for right, num in enumerate(nums):
            while mxq and mxq[-1] < num:
                mxq.pop()
            while mnq and mnq[-1] > num:
                mnq.pop()
            mxq.append(num)
            mnq.append(num)
            if mxq[0] - mnq[0] > limit:
                if mxq[0] == nums[left]:
                    mxq.popleft()
                if mnq[0] == nums[left]:
                    mnq.popleft()
                left += 1
        return len(nums) - left
