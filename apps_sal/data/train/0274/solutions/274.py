from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        start = 0
        end = 0
        res = 0

        max_q = deque()
        min_q = deque()

        while end < len(nums):
            while max_q and nums[max_q[-1]] <= nums[end]:
                max_q.pop()
            while min_q and nums[min_q[-1]] >= nums[end]:
                min_q.pop()

            max_q.append(end)
            min_q.append(end)

            # print(\"1\", max_q, min_q)
            while nums[max_q[0]] - nums[min_q[0]] > limit:
                start += 1
                if start > max_q[0]:
                    max_q.popleft()
                if start > min_q[0]:
                    min_q.popleft()

                # print(\"2\", max_q, min_q)

            print((end - start + 1))
            res = max(res, end - start + 1)
            end += 1

        return res
