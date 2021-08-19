class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        res = 0
        left, right = 0, 0
        inc, dec = collections.deque(), collections.deque()
        while right < n:
            while inc and nums[inc[-1]] >= nums[right]:  # 允许相同元素存在，这样的话滑动窗口pop的时候才能正确的pop完，否则会出现过早的pop完但left还没跟上的情况
                inc.pop()
            inc.append(right)
            while dec and nums[dec[-1]] <= nums[right]:
                dec.pop()
            dec.append(right)
            right += 1
            while nums[dec[0]] - nums[inc[0]] > limit:
                if inc[0] == left:
                    inc.popleft()
                if dec[0] == left:
                    dec.popleft()
                left += 1
            res = max(res, right - left)
            # print(left, right, res, inc, dec, )
        return res
