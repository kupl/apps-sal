class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)

        m = total % p
        if m == 0:
            return 0

        current_sum = 0
        IMPOSSIBLE = len(nums)
        ans = IMPOSSIBLE
        mod_last_positions = {0: -1}

        for idx, num in enumerate(nums):
            current_sum += num
            if (current_sum - m) % p in mod_last_positions:
                ans = min(ans, idx - mod_last_positions[(current_sum - m) % p])
            mod_last_positions[current_sum % p] = idx

        return ans if ans != IMPOSSIBLE else -1
