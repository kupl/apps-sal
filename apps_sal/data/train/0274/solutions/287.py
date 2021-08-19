import heapq


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0
        max_len = 1
        (i, j) = (0, 0)
        min_heap = []
        max_heap = []
        max_n = min_n = nums[0]
        while i <= j and j < len(nums):
            if max_n - min_n <= limit:
                max_len = max(max_len, j - i + 1)
                j += 1
                if j == len(nums):
                    continue
                if nums[j] > max_n:
                    max_n = nums[j]
                    heapq.heappush(min_heap, (nums[j], j))
                elif nums[j] < min_n:
                    min_n = nums[j]
                    heapq.heappush(max_heap, (-nums[j], j))
                else:
                    heapq.heappush(min_heap, (nums[j], j))
                    heapq.heappush(max_heap, (-nums[j], j))
            else:
                if nums[i] == max_n:
                    while True:
                        (max_n, s) = heapq.heappop(max_heap)
                        if s > i:
                            max_n *= -1
                            break
                elif nums[i] == min_n:
                    while True:
                        (min_n, t) = heapq.heappop(min_heap)
                        if t > i:
                            break
                i += 1
        return max_len
