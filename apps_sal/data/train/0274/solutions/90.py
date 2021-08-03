class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_len, start, end = 1, 0, 0
        pqmin, pqmax = [], []

        for end in range(len(nums)):
            heapq.heappush(pqmin, (nums[end], end))
            heapq.heappush(pqmax, (-nums[end], end))

            while start < end and abs(pqmax[0][0] + pqmin[0][0]) > limit:
                start += 1
                while pqmax and pqmax[0][1] < start:
                    heapq.heappop(pqmax)
                while pqmin and pqmin[0][1] < start:
                    heapq.heappop(pqmin)

            max_len = max(max_len, end - start + 1)

        return max_len
