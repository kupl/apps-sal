from collections import deque


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        asc = deque()
        dsc = deque()
        ret = l = 0
        for i in range(len(nums)):
            n = nums[i]
            while asc and n < asc[-1]:
                asc.pop()
            asc.append(n)
            while dsc and n > dsc[-1]:
                dsc.pop()
            dsc.append(n)
            while dsc[0] - asc[0] > limit:
                if dsc[0] == nums[l]:
                    dsc.popleft()
                if asc[0] == nums[l]:
                    asc.popleft()
                l += 1
            ret = max(ret, i - l + 1)
        return ret
