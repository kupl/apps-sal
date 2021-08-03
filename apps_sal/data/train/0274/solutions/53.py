from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        hq = deque()
        hq.append([nums[0], 0])
        lq = deque()
        lq.append([nums[0], 0])
        l = 0

        ans = 1
        for i in range(1, len(nums)):
            n = nums[i]
            while hq[0][1] < l:
                hq.popleft()
            while lq[0][1] < l:
                lq.popleft()

            while hq and hq[-1][0] <= n:
                hq.pop()
            else:
                hq.append([n, i])

            while lq and lq[-1][0] >= n:
                lq.pop()
            else:
                lq.append([n, i])

            if hq[0][0] - n > limit:
                ans = max(ans, i - l)
                while hq[0][0] - n > limit:
                    l = hq[0][1] + 1
                    hq.popleft()
            elif n - lq[0][0] > limit:
                ans = max(ans, i - l)
                while n - lq[0][0] > limit:
                    l = lq[0][1] + 1
                    lq.popleft()
            else:
                ans = max(ans, i - l + 1)

        return ans
