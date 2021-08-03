from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #         lhs = 0
        #         rhs = 1
        #         diff_len = 1
        #         sd = SortedList([nums[lhs]]) # map value -> count
        #         while rhs < len(nums):
        #             # print(f\"lhs: {lhs}, rhs: {rhs}\")
        #             sd.add(nums[rhs])
        #             # print(sd)
        #             if (sd[len(sd)-1] - sd[0] <= limit):
        #                 # print(f\"{sd[len(sd)-1]}-{sd[0]} > {limit}\")

        #                 diff_len = max(diff_len, rhs-lhs+1)
        #                 # print(f\"diff_len {diff_len}\")

        #             else:
        #                 sd.discard(nums[lhs])
        #                 lhs += 1
        #             rhs += 1
        #         return diff_len
        maxq, minq = [], []
        res = i = 0
        for j, a in enumerate(nums):
            heapq.heappush(maxq, [-a, j])
            heapq.heappush(minq, [a, j])
            while -maxq[0][0] - minq[0][0] > limit:
                i = min(maxq[0][1], minq[0][1]) + 1
                while maxq[0][1] < i:
                    heapq.heappop(maxq)
                while minq[0][1] < i:
                    heapq.heappop(minq)
            res = max(res, j - i + 1)
        return res
