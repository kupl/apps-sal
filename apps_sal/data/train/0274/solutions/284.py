class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_q = deque()
        min_q = deque()
        left = 0
        result = 0
        for (i, n) in enumerate(nums):
            while max_q and nums[max_q[-1]] <= n:
                max_q.pop()
            max_q.append(i)
            while min_q and nums[min_q[-1]] >= n:
                min_q.pop()
            min_q.append(i)
            while left < i and nums[max_q[0]] - nums[min_q[0]] > limit:
                if left == max_q[0]:
                    max_q.popleft()
                elif left == min_q[0]:
                    min_q.popleft()
                left += 1
            result = max(result, i - left + 1)
        return result
