class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        from heapq import heappop, heappush
        res = j = 0
        m = []
        n = []
        for i in range(len(nums)):
            x = nums[i]
            heappush(m, (-x, i))
            heappush(n, (x, i))
            while abs(-m[0][0] - n[0][0]) > limit:
                j = min(m[0][1], n[0][1]) + 1
                while j > m[0][1]:
                    heappop(m)
                while j > n[0][1]:
                    heappop(n)
            res = max(res, i - j + 1)

        return res
