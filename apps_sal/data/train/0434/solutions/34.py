class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        prev, curr, best = 0, 0, 0
        n = len(nums)
        for i, x in enumerate(nums):
            if x == 0:
                best = max(best, prev + curr)

                if i == n - 1:
                    pass

                elif nums[i + 1] == 1:  # this is a gap
                    prev = curr
                    curr = 0
                else:
                    prev = 0
                    curr = 0
            else:
                curr += 1

        best = max(best, prev + curr)

        if best == n:  # all ones, need to remove one element at least
            best -= 1

        return best
