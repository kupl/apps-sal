from collections import deque


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        N = len(nums)
        ans = 0
        maxi = deque()  # decreasing 9 5 1
        mini = deque()  # increasing 1 5 9
        j = 0

        for i in range(N):
            while mini and nums[i] < nums[mini[-1]]:
                mini.pop()

            while maxi and nums[i] > nums[maxi[-1]]:
                maxi.pop()

            mini.append(i)
            maxi.append(i)

            if abs(nums[maxi[0]] - nums[mini[0]]) <= limit:
                ans = max(ans, abs(maxi[0] - mini[0]) + 1)
            else:
                # remove elements outside of the window
                while mini and mini[0] <= j:
                    mini.popleft()
                while maxi and maxi[0] <= j:
                    maxi.popleft()
                j += 1

        return N - j
