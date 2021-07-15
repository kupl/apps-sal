class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = 0
        min_dq = deque()
        max_dq = deque()
        out = 0
        for r in range(len(nums)):
            val = nums[r]
            while min_dq and val < nums[min_dq[-1]]:
                min_dq.pop()
            while max_dq and val > nums[max_dq[-1]]:
                max_dq.pop()
            max_dq.append(r)
            min_dq.append(r)
            while nums[max_dq[0]]-nums[min_dq[0]] > limit:
                l+=1
                if max_dq[0] < l:
                    max_dq.popleft()
                if min_dq[0] < l:
                    min_dq.popleft()
            out = max(out, r-l+1)
        return out
