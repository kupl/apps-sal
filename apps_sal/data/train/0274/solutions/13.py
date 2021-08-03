import collections


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        minDeque = collections.deque()
        maxDeque = collections.deque()

        start = end = 0

        ans = 0

        while end < len(nums):
            # print(start, end, ans)
            n = nums[end]
            while len(minDeque) > 0 and nums[minDeque[-1]] >= n:
                minDeque.pop()

            minDeque.append(end)

            while len(maxDeque) > 0 and nums[maxDeque[-1]] <= n:
                maxDeque.pop()

            maxDeque.append(end)

            if (nums[maxDeque[0]] - nums[minDeque[0]]) > limit:
                start += 1

                while len(minDeque) > 0 and minDeque[0] < start:
                    minDeque.popleft()

                while len(maxDeque) > 0 and maxDeque[0] < start:
                    maxDeque.popleft()
            else:
                ans = max(ans, (end - start) + 1)
                end += 1

        return ans
