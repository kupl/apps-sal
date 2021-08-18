from heapq import heappush, heapify, heappop


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_subsize, right, left = 0, 0, 0
        max_vals, min_vals = [], []
        heapify(max_vals)
        heapify(min_vals)

        while right < len(nums):
            diff = max_vals[0][0] * -1 - min_vals[0][0] if max_vals and min_vals else 0
            if diff <= limit:
                max_subsize = max(max_subsize, right - left)
                heappush(min_vals, (nums[right], right))
                heappush(max_vals, (nums[right] * -1, right))
                right += 1
            else:
                left += 1
                while max_vals and max_vals[0][1] < left:
                    heappop(max_vals)
                while min_vals and min_vals[0][1] < left:
                    heappop(min_vals)
            diff = max_vals[0][0] * -1 - min_vals[0][0] if max_vals and min_vals else 0
            if diff <= limit:
                max_subsize = max(max_subsize, right - left)

        return max_subsize
