class Solution:
    def minOperations(self, nums: List[int]) -> int:

        def n1b(x):
            ans = 0
            while x:
                x &= (x - 1)
                ans += 1
            return ans

        def hi(x):
            ans = 0
            while x:
                x >>= 1
                ans += 1
            return ans

        maxshift = 0
        tog = 0
        for n in nums:
            maxshift = max(maxshift, hi(n))
            tog += n1b(n)

        maxshift = max(0, maxshift - 1)
        return maxshift + tog
