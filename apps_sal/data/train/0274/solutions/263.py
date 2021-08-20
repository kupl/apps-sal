class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        start_pos = 0
        (inc, dec) = (deque([]), deque([]))
        for i in range(len(nums)):
            while len(inc) > 0 and nums[inc[-1]] > nums[i]:
                inc.pop()
            inc.append(i)
            while len(dec) > 0 and nums[dec[-1]] < nums[i]:
                dec.pop()
            dec.append(i)
            while abs(nums[inc[0]] - nums[dec[0]]) > limit:
                start_pos += 1
                if inc[0] < start_pos:
                    inc.popleft()
                if dec[0] < start_pos:
                    dec.popleft()
            ans = max(ans, i - start_pos + 1)
        return ans
