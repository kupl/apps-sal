class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l = ans = 0
        maxh, minh = [], []
        for r, num in enumerate(nums):
            heapq.heappush(maxh, (-1 * num, r))
            heapq.heappush(minh, (num, r))

            while maxh[0][0] * -1 - minh[0][0] > limit:
                while maxh[0][1] <= l:
                    heapq.heappop(maxh)
                while minh[0][1] <= l:
                    heapq.heappop(minh)
                l += 1

            ans = max(ans, r - l + 1)

        return ans
