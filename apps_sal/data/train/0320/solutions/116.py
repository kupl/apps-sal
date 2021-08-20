class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def count(n):
            a = b = 0
            while n:
                if n & 1:
                    n -= 1
                    b += 1
                else:
                    n >>= 1
                    a += 1
            return (a, b)
        maxA = sumB = 0
        for n in nums:
            (a, b) = count(n)
            maxA = max(maxA, a)
            sumB += b
        return maxA + sumB
