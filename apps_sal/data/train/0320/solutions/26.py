class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # TC: O(NlogM), SC: O(1), n = len(nums), m = max(nums)
        def numOperations(x):
            # TC: O(logX)
            n1, n2 = 0, 0
            while x:
                if x & 1:
                    n1 += 1
                    x -= 1
                else:
                    n2 += 1
                    x //= 2
            return n1, n2
        # operation -1 is self, //2 is shared.
        n1, n2 = 0, 0
        for x in nums:
            x1, x2 = numOperations(x)
            n1 += x1
            n2 = max(n2, x2)
        return n1 + n2
