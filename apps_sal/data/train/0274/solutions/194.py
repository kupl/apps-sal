import heapq


class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        ans = 0
        heap1 = []
        heap2 = []
        end = 0
        start = 0
        n = len(nums)
        while end < n:
            heapq.heappush(heap1, [-nums[end], end])
            heapq.heappush(heap2, [nums[end], end])
            while -heap1[0][0] - heap2[0][0] > limit:
                start += 1
                while heap1 and heap1[0][1] < start:
                    heapq.heappop(heap1)
                while heap2 and heap2[0][1] < start:
                    heapq.heappop(heap2)
            ans = max(ans, end - start + 1)
            end += 1
        return ans
