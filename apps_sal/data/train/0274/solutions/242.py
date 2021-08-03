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
                if nums[l] == dsc[0]:
                    dsc.popleft()
                if nums[l] == asc[0]:
                    asc.popleft()
                l += 1
            ret = max(ret, i - l + 1)
        return ret
