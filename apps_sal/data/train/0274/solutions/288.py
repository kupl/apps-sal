class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        (VALUE, INDEX) = (0, 1)
        left = 0
        (min_h, max_h) = ([], [])
        max_len = 0
        for (right, num) in enumerate(nums):
            heappush(min_h, (num, right))
            heappush(max_h, (-num, right))
            while -max_h[0][VALUE] - min_h[0][VALUE] > limit:
                if max_h[0][INDEX] < min_h[0][INDEX]:
                    left = heappop(max_h)[INDEX] + 1
                else:
                    left = heappop(min_h)[INDEX] + 1
                while min_h[0][INDEX] < left:
                    heappop(min_h)
                while max_h[0][INDEX] < left:
                    heappop(max_h)
            max_len = max(max_len, right - left + 1)
        return max_len
