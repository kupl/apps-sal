from queue import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        if len(nums) == 1:
            return 1

        print(nums)
        decreasing = deque()
        increasing = deque()

        max_l = 1
        if abs(nums[1] - nums[0]) <= limit:
            max_l = 2

        p0 = 0
        p1 = 0

        while p1 <= len(nums) - 1:

            while decreasing and nums[decreasing[-1]] < nums[p1]:
                decreasing.pop()
            while increasing and nums[increasing[-1]] > nums[p1]:
                increasing.pop()

            while decreasing and decreasing[0] < p0:
                decreasing.popleft()
            while increasing and increasing[0] < p0:
                increasing.popleft()

            decreasing.append(p1)
            increasing.append(p1)

            while p0 < p1 and nums[decreasing[0]] - nums[increasing[0]] > limit:
                if decreasing[0] == p0:
                    decreasing.popleft()
                if increasing[0] == p0:
                    increasing.popleft()
                p0 += 1

            if nums[decreasing[0]] - nums[increasing[0]] <= limit:
                max_l = max(max_l, p1 - p0 + 1)
            p1 += 1

        return max_l
