from functools import lru_cache


class Solution:

    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        d = {0: {x: i for (i, x) in enumerate(nums1)}, 1: {x: i for (i, x) in enumerate(nums2)}}
        arrs = [nums1, nums2]
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(i, j):
            res = 0
            while j < len(d[i]):
                val = arrs[i][j]
                if val not in d[1 - i]:
                    res += val
                else:
                    k = d[1 - i][val]
                    res += val + max(dp(1 - i, k + 1), dp(i, j + 1))
                    return res
                j += 1
            return res
        return max(dp(0, 0), dp(1, 0)) % MOD
