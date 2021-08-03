class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        ans, m, j, cur = 0, {0: -1}, -1, 0
        for i, x in enumerate(nums):
            cur += x
            k = cur - target
            if k in m and m[k] >= j:
                ans += 1
                j = i
            m[cur] = i
        return ans
