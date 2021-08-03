class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        elif len(nums) == 5:
            nums_sorted = sorted(nums)
            diff = []
            for i in range(1, len(nums)):
                diff.append(nums_sorted[i] - nums_sorted[i - 1])
            return min(diff)
        else:
            largest_four = []
            smallest_four = []
            for n in nums:
                if len(largest_four) < 4:
                    heapq.heappush(largest_four, n)
                    heapq.heappush(smallest_four, -n)
                else:
                    heapq.heappushpop(largest_four, n)
                    heapq.heappushpop(smallest_four, -n)
            smallest_four = sorted([-x for x in smallest_four])
            largest_four = sorted(largest_four)

            diff_arr = [largest_four[0] - smallest_four[0],
                        largest_four[3] - smallest_four[3],
                        largest_four[1] - smallest_four[1],
                        largest_four[2] - smallest_four[2]]

        return min(diff_arr)
