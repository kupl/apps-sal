class Solution:
    def getMaxLen(self, nums: List[int]) -> int:

        a = 0
        p = 0
        n = 0
        r = -1

        for x in nums:
            p, n, r = (
                (x < 0) * p + (x > 0) * (p + 1),
                (x < 0) * (n + 1) + (x > 0) * n,
                (x < 0) * (r < 0) * p + (x < 0) * (r >= 0) * r + (x > 0) * r - (x == 0)
            )

            a = max(a, p + n - (n % 2) * (r + 1))

        return a
