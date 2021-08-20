class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 1
        st = en = 0
        min_q = collections.deque()
        max_q = collections.deque()
        while en < len(nums):
            while min_q and nums[en] <= nums[min_q[-1]]:
                min_q.pop()
            while max_q and nums[en] >= nums[max_q[-1]]:
                max_q.pop()
            min_q.append(en)
            max_q.append(en)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                st += 1
                if st > min_q[0]:
                    min_q.popleft()
                if st > max_q[0]:
                    max_q.popleft()
            ans = max(ans, en - st + 1)
            en += 1
        return ans
