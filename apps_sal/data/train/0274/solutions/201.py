from sortedcontainers import SortedList


class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        lhs = 0
        rhs = 1
        diff_len = 1
        sd = SortedList([nums[lhs]])  # map value -> count
        while rhs < len(nums):
            # print(f\"lhs: {lhs}, rhs: {rhs}\")
            sd.add(nums[rhs])
            # print(sd)
            if (sd[len(sd) - 1] - sd[0] <= limit):
                # print(f\"{sd[len(sd)-1]}-{sd[0]} > {limit}\")

                diff_len = max(diff_len, rhs - lhs + 1)
                # print(f\"diff_len {diff_len}\")

            else:
                sd.discard(nums[lhs])
                lhs += 1
            rhs += 1
        return diff_len
