import heapq

# minMaxQueue:
# max 4 5
# min 4 3 3 2
#     queue: [1, 6, 8, 2, 2]


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        longest = 0
        mins = []
        maxs = []
        start = 0
        i = 0
        while i < len(nums):
            x = nums[i]
            heapq.heappush(mins, (x, i))
            heapq.heappush(maxs, (-x, i))

            currMin, currMax = mins[0][0], -(maxs[0][0])
            while mins and maxs and currMax - currMin > limit:
                start += 1
                while mins[0][1] < start:
                    heapq.heappop(mins)
                while maxs[0][1] < start:
                    heapq.heappop(maxs)

                currMin, currMax = mins[0][0], -(maxs[0][0])

            longest = max(longest, i - start + 1)
            i += 1

        return longest
