import heapq


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        max_d = 0
        min_heap = [nums[0]]
        max_heap = [-nums[0]]
        local_max = nums[0]
        local_min = nums[0]
        while left < n and right < n:
            if nums[right] > local_max:
                local_max = nums[right]
            if nums[right] < local_min:
                local_min = nums[right]
            lower = local_max - limit
            upper = local_min + limit
            if lower <= nums[right] <= upper:
                if right - left + 1 > max_d:
                    max_d = right - left + 1
                right += 1
                if right < n:
                    heapq.heappush(min_heap, nums[right])
                    heapq.heappush(max_heap, -nums[right])
            else:
                if nums[left] == min_heap[0]:
                    heapq.heappop(min_heap)
                else:
                    min_heap.remove(nums[left])
                if max_heap[0] == -nums[left]:
                    heapq.heappop(max_heap)
                else:
                    max_heap.remove(-nums[left])
                left += 1
                local_min = min_heap[0]
                local_max = -max_heap[0]
        return max_d
