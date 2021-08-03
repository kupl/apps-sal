class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        if not nums:
            return 0

        n = len(nums)
        i = j = 0
        curr_max = curr_min = nums[0]
        maxes = [(-curr_max, 0)]
        mins = [(curr_min, 0)]
        best = 0

        while i <= j < n:
            # print(\"i\", i, \"j\", j, \"max:\", -maxes[0][0], \"at idx\", maxes[0][1], \"min:\", mins[0][0], \"at idx\", mins[0][1])

            # advance j until difference exceeds limit
            if abs(-maxes[0][0] - mins[0][0]) <= limit:
                best = max(best, j - i + 1)
                j += 1

                if j < n:
                    heapq.heappush(maxes, (-nums[j], j))
                    heapq.heappush(mins, (nums[j], j))
            else:
                i += 1

                # lazily remove all values outside of the window
                while not i <= maxes[0][1] <= j:
                    heapq.heappop(maxes)
                while not i <= mins[0][1] <= j:
                    heapq.heappop(mins)

        return best
