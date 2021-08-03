class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        nums = A
        flip_count = 0
        flip_hint = [0] * len(nums)
        total_flips = 0

        for i, n in enumerate(nums):
            if i >= K and flip_hint[i - K]:
                total_flips -= 1

            if total_flips % 2 == n:
                if i + K > len(nums):
                    return -1

                total_flips += 1
                flip_hint[i] = 1
                flip_count += 1

        return flip_count
