class Solution:

    def minOperations(self, nums: List[int]) -> int:

        def do(n):
            (a, b) = (0, 0)
            while n != 0:
                if n % 2 == 1:
                    a += 1
                    n -= 1
                else:
                    b += 1
                    n //= 2
            return [a, b]
        (aa, bb) = (0, 0)
        for n in nums:
            (a, b) = do(n)
            aa += a
            bb = max(b, bb)
        return aa + bb
