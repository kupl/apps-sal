class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def numOperations(x):
            n1, n2 = 0, 0
            while x:
                if x & 1:
                    n1 += 1
                    x -= 1
                else:
                    n2 += 1
                    x >>= 1
            return n1, n2
        n1, n2 = 0, 0
        for x in nums:
            x1, x2 = numOperations(x)
            n1 += x1
            n2 = max(n2, x2)
        return n1 + n2
