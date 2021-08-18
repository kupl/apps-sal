import heapq


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        '''
        Find the longest non-empty subarray s where max(s) - min(s) <= limit
        '''
        max_q, min_q = [[nums[0], 0]], [[nums[0], 0]]
        ans = 1
        i = j = 0
        while j < len(nums):
            heapq.heappush(max_q, [-nums[j], j])
            heapq.heappush(min_q, [nums[j], j])
            if -max_q[0][0] - min_q[0][0] <= limit:
                ans = max(ans, j - i + 1)
                j += 1
            else:
                i = min(max_q[0][1], min_q[0][1]) + 1
                while max_q[0][1] < i:
                    heapq.heappop(max_q)
                while min_q[0][1] < i:
                    heapq.heappop(min_q)
        return ans
